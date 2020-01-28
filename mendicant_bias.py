import os
import time
import re
import slack
import network
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
    
    if "subtype" in data:
        return

    web_client = payload['web_client']
    
    command_tokens = tokenize_command(data['text'])
    module = route_command(data, web_client)
    text = module(command_tokens)
    web_client.chat_postMessage(channel=data['channel'], text=text)

def route_command(data, webclient):
    channel = data['channel']

    switcher={
        channels['network']:network.handle_command 
    }

    return switcher.get(channel, invalid_module)

def tokenize_command(command_string):
	return command_string.split()

def invalid_module():
    return "I'm sorry Reclaimer, I don't have subroutines for that module"
if __name__ == "__main__":
    convo_list = web_client.api_call("conversations.list")
    channels = {channel['name']: channel['id'] for channel in convo_list['channels']}
    rtm_client.start()

