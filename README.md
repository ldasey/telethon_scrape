Scripts are provided which enable social scientists to easily retrieve data from the chat service Telegram for a known population on a large scale. Scraping of public as well as private channels and groups is possible as long as group name or invite identification are known. Output is to a .csv-file (optionally SQL).

The scripts require `Python 3` and the [Telethon](https://github.com/LonamiWebs/Telethon/) and [pandas](https://github.com/pandas-dev/pandas) libraries.

# setup

1. Sign up for Telegram
2. Log in [here](https://my.telegram.org/auth), create an application and retrieve your API ID and hash
3. Create a string session and retrieve your identification string which is described [here in Telethon documentation](https://docs.telethon.dev/en/latest/concepts/sessions.html)
4. Enter these three identification credentials into `config.py` which is then easily accessed through `import config` in the main scripts
5. Create a .txt-file in the sub directory `/lists/`. One row should contain exactly one channel/group name in the case of `scrape_public.py` and one group invite ID in the case of `scrape_private.py`
6. Create a subdirectory called `/log/` to which the log file will be saved
7. Create a subdirectory called `/csv/` to which the output .csv-file will be saved
