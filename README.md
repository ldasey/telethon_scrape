Scripts are provided which enable social scientists to easily retrieve chat data from the service Telegram for a known population on a large scale. Scraping of public as well as private channels and groups is possible as long as group name or invite identification are known. Output is to a .csv-file.

These are sample scripts from a larger project of mine which includes some automation as well as SQL integration. I might integrate the framework I use into additional branches some time.

`scrape_public.py` can be used for obtaining chats from public groups which everyone can access and which can be found through Telegram's search engine. `scrape_private.py` can be used to scrape private chats that require an invitation link. The invite link which goes as input into the script is the last part of the link after the `/`.

The scripts require `Python 3` and the [Telethon](https://github.com/LonamiWebs/Telethon/) and [pandas](https://github.com/pandas-dev/pandas) libraries.

# setup

1. Sign up for Telegram
2. Log in [here](https://my.telegram.org/auth), create an application and retrieve your API ID and hash
3. Create a string session and retrieve your identification string which is described [here in Telethon documentation](https://docs.telethon.dev/en/latest/concepts/sessions.html)
4. Enter these three identification credentials into `config.py` which is then easily accessed through `import config` in the main scripts
5. Create a .txt-file in the sub directory `/lists/`. One row should contain exactly one channel/group name in the case of `scrape_public.py` and one group invite ID in the case of `scrape_private.py`
6. Create a subdirectory called `/log/` to which the log file will be saved. The name of the log file can be specified in the variable `logname` in the main script
7. Create a subdirectory called `/csv/` to which the output .csv-file will be saved. The name of the output csv file can be specified in the variable `csvname` in the main script

Inputs of the configuration variables `is_invite` and `wave` are just saved to a column of the pd.dataframe and are not mandatory.

For further information on the data retrieved consult the Telethon documentation [here](https://docs.telethon.dev/en/latest/quick-references/events-reference.html) and [here](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html).
