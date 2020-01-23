import os
import time
import re
import slack
from dotenv import load_dotenv

#load env variables
load_dotenv()

#setup RTM client
slack_token = os.getenv("SLACK_BOT_TOKEN")
rtm_client = slack.RTMClient(token=slack_token)
web_client = slack.WebClient(slack_token)
mendicant_id = web_client.api_call("auth.test")["user_id"]
channels = {} 

@slack.RTMClient.run_on(event='message')
def unpack_payload(**payload):
    """
        executes bot command if teh command is known
    """

    data = payload['data']
    web_client = payload['web_client']

    message = handle_command(data, web_client)

    default_response = "How unfortunate, Reclaimer, that command is not known"
    
    if not "subtype" in data:
        web_client.chat_postMessage(channel=data['channel'], text=message)

def handle_command(data, webclient):
    channel = data['channel']

    switcher={
        channels['network']: 'you made it!'
    }

    return switcher.get(channel, 'I N V A L I D')

if __name__ == "__main__":
    convo_list = web_client.api_call("conversations.list")
    channels = {channel['name']: channel['id'] for channel in convo_list['channels']}
    rtm_client.start()

