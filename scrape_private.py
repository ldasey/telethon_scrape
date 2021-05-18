# import relevant libraries

import sys
import pandas as pd
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import CheckChatInviteRequest
import time
import telethon.utils as utils

import logging
import datetime


# import sql und telegram login
import config



### configuration:

#name of the logfile (.txt). Logfile is saved in sub directory /log/
logname = 'wave2_private'

#input for scaping: (.txt) One group/channel per line. File should be in sub directory /lists/
listname = 'wave1_private'

# .csv output (.csv). File will be saved to sub directory /csv/
csvname = 'wave2_private'

# invite link required? (1=yes)
is_invite = 1

# wave, useful if script is executed repeatedly
wave = 1

# sleep after loop (in secs). Time out is useful as to not make Telegram believe we are a bot
sleep = 361


#log: will be saved to sub directory /log/

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('log/' + logname + '_' + datetime.datetime.now().strftime("%d.%m.%Y_%H.%M") + '.txt', 'a'))
print = logger.info

# check if script is executed rightfully, as SQL content might get removed

continuescript = input('Would you like to continue with this script? (Y/n)')

if continuescript in ['Y', 'y']:
    print('Great. lets continue')
else:
    sys.exit()


time.sleep(5.5)


# read in input for scraping
lineList = [line.rstrip('\n') for line in open("lists/" + listname + '.txt')]

chats = lineList


# the actual scraping process
client = TelegramClient(StringSession(config.string), config.api_id, config.api_hash)

async def main():
    for chat in chats:
        time.sleep(5)
        try:
            # try to join
            await client(ImportChatInviteRequest(chat))
            time.sleep(5)
        except:
            print(chat + ' channel/group does not exist or other error. Skipping to next channel...')
        else:
            # if join successful, retrieve chat title
            chatinvite = await client(CheckChatInviteRequest(hash = chat))

            try:
                chattitle = chatinvite.channel.title
            except:
                chattitle = chatinvite.chat.title
                print(chattitle + ' seems to be a chat...')

            time.sleep(10)
            print('Successfully joined ' + chattitle + '. Starting scraping now...')
            list = []
            async for message in client.iter_messages(chattitle, reverse=True):
                list.append([chattitle, message.chat_id, message.is_private, message.is_group, message.is_channel, is_invite, wave, message.id,
                             message.sender_id, message.date, message.text, message.action])
            df = pd.DataFrame(list)
            df.columns = ['chat_title', 'chat_id', 'is_private', 'is_group', 'is_channel', 'is_invite', 'wave', 'message_id', 'message_senderid',
                          'message_date', 'message_text', 'message_action']
            df['message_action'] = df['message_action'].astype(str)

        time.sleep(sleep)


with client:
    client.loop.run_until_complete(main())

time.sleep(5.5)


# save data to .csv-file. Can be removed if no .csv output is wished
try:
    df.to_csv('csv/' + csvname + '.csv', sep = '-')
except:
    print('Was not able to write .csv')
else:
    print('everything worked like a charm. .csv file saved.')
