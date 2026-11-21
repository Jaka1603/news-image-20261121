#!/usr/bin/env python3
"""Penjaga gerbang gambar untuk entri harian.

Program kecil ini mengambil berkas bernama image.jpg yang tinggal
di folder yang sama dengan skrip ini, memeriksanya secara menyeluruh,
lalu meneruskannya apa adanya ke /output/entry.png hanya apabila
semua pemeriksaan lolos. Pemeriksaan yang dilakukan meliputi
keberadaan berkas, batas ukuran, pengenalan format lewat tanda
awal berkas (bukan lewat nama), serta pembacaan ukuran piksel
langsung dari kepala gambar. Sesudah penyalinan, isi berkas tujuan
dibaca ulang dan sidik jarinya dibandingkan supaya salinan yang
rusak tidak pernah dianggap berhasil.
"""

import hashlib
import os
import struct
import sys

BATAS_UKURAN = 1048576
BATAS_SISI = 1024
TUJUAN = os.path.join(os.sep + "output", "entry.png")

TANDA_JPEG = b"\xff\xd8\xff"
TANDA_PNG = b"\x89PNG\r\n\x1a\n"

# Penanda segmen JPEG yang membawa kerangka gambar (start of frame),
# di luar penanda yang dikecualikan menurut kebiasaan formatnya:
# C4 (tabel Huffman), C8 (ekstensi), dan CC (pengkodean aritmetika).
PENANDA_KERANGKA = {
    0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
    0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
}


def gagal(pesan):
    """Tulis pesan kegagalan ke stderr dan hentikan program."""
    sys.stderr.write("error: " + pesan + "\n")
    raise SystemExit(1)


def kenali_format(isi):
    """Tentukan nama format dari byte awal, atau gagal."""
    if isi[:3] == TANDA_JPEG:
        return "JPEG"
    if isi[:8] == TANDA_PNG:
        return "PNG"
    gagal("format tidak dikenali: tanda awal bukan JPEG maupun PNG")


def ukuran_png(isi):
    """Ambil lebar dan tinggi dari potongan IHDR sebuah PNG."""
    # Tata letak: 8 byte tanda, lalu potongan pertama wajib IHDR:
    # 4 byte panjang data, 4 byte nama potongan, baru lebar/tinggi.
    if len(isi) < 24:
        gagal("berkas PNG terlalu pendek untuk memuat IHDR")
    if isi[12:16] != b"IHDR":
        gagal("potongan pertama PNG bukan IHDR")
    lebar = struct.unpack(">I", isi[16:20])[0]
    tinggi = struct.unpack(">I", isi[20:24])[0]
    return lebar, tinggi


def ukuran_jpeg(isi):
    """Telusuri segmen JPEG sampai kerangka gambar ditemukan."""
    # Sesudah dua byte SOI, tiap segmen diawali 0xFF lalu byte penanda.
    # Kebanyakan segmen membawa panjang dua byte (termasuk kedua byte
    # panjang itu sendiri); segmen mandiri tidak membawa panjang.
    posisi = 2
    panjang_total = len(isi)
    while posisi + 1 < panjang_total:
        if isi[posisi] != 0xFF:
            gagal("struktur JPEG rusak pada offset %d" % posisi)
        penanda = isi[posisi + 1]
        # Lewati byte pengisi 0xFF yang kadang berderet.
        while penanda == 0xFF and posisi + 2 < panjang_total:
            posisi += 1
            penanda = isi[posisi + 1]
        if penanda in PENANDA_KERANGKA:
            # Isi segmen kerangka: 1 byte ketelitian, lalu tinggi
            # dan lebar masing-masing dua byte big-endian.
            if posisi + 9 > panjang_total:
                gagal("segmen kerangka JPEG terpotong")
            tinggi = struct.unpack(">H", isi[posisi + 5:posisi + 7])[0]
            lebar = struct.unpack(">H", isi[posisi + 7:posisi + 9])[0]
            return lebar, tinggi
        if penanda == 0xD9 or penanda == 0xDA:
            break  # EOI atau awal data pindai: kerangka sudah lewat.
        if penanda == 0x01 or 0xD0 <= penanda <= 0xD8:
            posisi += 2  # Segmen mandiri tanpa kolom panjang.
            continue
        if posisi + 4 > panjang_total:
            gagal("kepala segmen JPEG terpotong")
        panjang_segmen = struct.unpack(">H", isi[posisi + 2:posisi + 4])[0]
        if panjang_segmen < 2:
            gagal("panjang segmen JPEG tidak masuk akal")
        posisi += 2 + panjang_segmen
    gagal("segmen kerangka (start-of-frame) tidak ditemukan pada JPEG")


def periksa_berkas(lokasi):
    """Baca berkas sumber dan jalankan seluruh validasi atasnya."""
    if not os.path.isfile(lokasi):
        gagal("berkas tidak ditemukan: " + lokasi)
    # Tolak berkas kosong dan berkas raksasa dari metadatanya dulu,
    # sebelum isinya dimuat ke memori sama sekali.
    ukuran_di_disk = os.path.getsize(lokasi)
    if ukuran_di_disk == 0:
        gagal("berkas kosong: " + lokasi)
    if ukuran_di_disk > BATAS_UKURAN:
        gagal(
            "berkas terlalu besar: %d byte (batas %d byte)"
            % (ukuran_di_disk, BATAS_UKURAN)
        )
    with open(lokasi, "rb") as pegangan:
        isi = pegangan.read()
    if len(isi) != ukuran_di_disk:
        gagal("ukuran berkas berubah saat dibaca: " + lokasi)
    jenis = kenali_format(isi)
    if jenis == "PNG":
        lebar, tinggi = ukuran_png(isi)
    else:
        lebar, tinggi = ukuran_jpeg(isi)
    for nama_sisi, nilai in (("lebar", lebar), ("tinggi", tinggi)):
        if nilai < 1 or nilai > BATAS_SISI:
            gagal(
                "%s gambar %d piksel di luar rentang 1..%d"
                % (nama_sisi, nilai, BATAS_SISI)
            )
    return isi, jenis, lebar, tinggi


def salin_dan_buktikan(isi):
    """Tulis byte ke tujuan lalu buktikan hasil tulisannya utuh."""
    folder = os.path.dirname(TUJUAN)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)
    with open(TUJUAN, "wb") as pegangan:
        pegangan.write(isi)
    sidik = hashlib.sha256(isi).hexdigest()
    with open(TUJUAN, "rb") as pegangan:
        terbaca = pegangan.read()
    sidik_ulang = hashlib.sha256(terbaca).hexdigest()
    if sidik_ulang != sidik:
        gagal("sidik SHA-256 hasil salinan tidak cocok dengan sumber")
    return sidik


def main():
    folder_skrip = os.path.dirname(os.path.abspath(__file__))
    sumber = os.path.join(folder_skrip, "image.jpg")
    isi, jenis, lebar, tinggi = periksa_berkas(sumber)
    sidik = salin_dan_buktikan(isi)
    sys.stdout.write(
        "%s %dx%d %d bytes sha256=%s\n"
        % (jenis, lebar, tinggi, len(isi), sidik)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
