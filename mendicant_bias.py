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

@slack.RTMClient.run_on(event='message')
def handle_command(**payload):
    """
        executes bot command if teh command is known
    """

    data = payload['data']
    web_client = payload['web_client']

    default_response = "How unfortunate, Reclaimer, that command is not known"
    
    if not "subtype" in data:
        web_client.chat_postMessage(channel=data['channel'], text=default_response)


rtm_client.start()

