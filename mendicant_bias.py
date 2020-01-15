import os
import time
import re
from slackclient import SlackClient

#setup slack client
slack = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
mendicant_bias_id = None

# constants
RTM_READ_DELAY = 1
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

if __name__ == "__main__":
    if slack.rtm_connect(with_team_state=False):
        print("Mendicant Bias connected and online.")
        mendicant_bias_id = slack.api_call("auth.test")["user_id"]
        while True:
            parse_bot_commands(slack.rtm_read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Mendicant Bias failed to connect. Please view logs and try again.")

def parse_bot_commands(slack_events):
    """
        parses a list of events coming from the slack stm api to find bot commands.
        if a bot command is found, this function returns a tuple of command and channel
        if its not found, then this function returns None, None.
    """

    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            handle_command(event["text"], event["channel"]

def handle_command(command, channel):
    """
        executes bot command if teh command is known
    """

    default_response = "How unfortuante, Reclaimer, that command is now known"

    response = None
    #if command.startswith(EXAMPLE_COMMAND):
    #    response = "Sure thing Reclaimer, as soon as the protocols are established I will enact them"
    
    slack.api_call("chat.postMessage", channel=channel, default_response)
