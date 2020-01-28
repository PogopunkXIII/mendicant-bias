import requests

#hardcoding this for now
url_base='http://localhost:5000/network/wol'

def handle_command(command_tokens):
    switcher={
        "wake":wake_command
    }
    
    command = switcher.get(command_tokens[0], invalid_command)
    return command(command_tokens[1])

def invalid_command(command_string):
    return "I'm sorry Reclaimer, but what you're asking isn't a supported subroutine for the Network module yet"

def wake_command(target):
    response = requests.post(url_base, json={'computer_name': target})
    return 'Reclaimer, executing the protocol to wake {}'.format(target)
        
