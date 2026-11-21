# The World Today — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Jaka1603/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Jaka1603/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

[![Daily News in One Image](https://img.shields.io/badge/Daily%20News-in%20One%20Image-black)](https://make.fun/bounties/news-image-20261121)
[![One Image](https://img.shields.io/badge/One-Image-black)](https://make.fun/bounties/news-image-20261121)
[![Python 3](https://img.shields.io/badge/Python%203-stdlib%20only-black)](https://make.fun/bounties/news-image-20261121)

## What it does

Saturday's whole front page, drawn as one black-and-white broadsheet.
Russia's biggest barrage of the war — more than 400 drones and 110
missiles, three Kyiv bridges hit — leads the page, next to the Russian
missile and drone that crossed into Polish, NATO airspace. Below them:
the Trump–Xi–Putin reconciliation declaration, the UK–EU reset deal,
California's subpoena of Nvidia, Saudi Arabia downing three Houthi
ballistic missiles over Riyadh, Myanmar's generals defying the world
court, America's measles surge toward 6,000 cases, Iraq's move on a
militia stronghold held for twelve years, the foiled Copenhagen plot,
the Berlin summit, and the US appeals court voiding the 2022 spending
law. A markets band carries the week's crash — Asia-Pacific down 8.5%,
Taiwan down 17%, Anthropic's record $81B IPO fading, Nvidia at a
52-week low — and a briefs column sweeps Sumy, Jakarta, Rome, Mexico
City, Khartoum, New Delhi, Caracas, Bayelsa and Kabul.

## The day's front page

The artwork is `image.jpg`: a masthead, a markets band with a ticker
tape, twelve illustrated story panels, a nine-item world briefs
column and a black footer bar with the EU's €1 billion military-aid
approval for Ukraine — every headline legible at thumbnail size.

## Run it

```
python3 main.py
```

The program checks the artwork against the competition's limits
(JPEG or PNG, at most 1 MiB, at most 1024×1024 px), copies it
byte-for-byte to `/output/entry.png`, then reads the copy back and
prints its SHA-256 so the written file is provably the artwork that
was checked. It uses only the Python 3 standard library.

## License

MIT — see `LICENSE`.
