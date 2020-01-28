import requests

#hardcoding this for now
url_base='https://localhost:5000/network/wake/'

def handle_command(command_tokens):
    switcher={
        "wake":wake_command
    }
    
    command = switcher.get(command_tokens[0], invalid_command)
    return command(command_tokens[1])

def invalid_command(command_string):
    return "I'm sorry Reclaimer, but what you're asking isn't a supported subroutine for the Network module yet"

def wake_command(target):
    return 'Reclaimer, executing the protocol to wake {}'.format(target)
    #response = requests.post('localhost:5000/network/wol', data={'computer_name': target})
        
