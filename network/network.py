import requests

#hardcoding this for now
url_base='https://localhost:5000/network/wake/'

def handle_command(command_tokens):
    switcher={
        "wake":wake_command
    }
    
    command = switcher.get(command_tokens[0], invalid_command)

    command(command_tokens[1])

def invalid_command(command_string):
    print("I'm sorry Reclaimer, but {} isn't a support subroutine for the Network module yet", command_string)

def wake_command(target):
    print('Reclaimer, you asked me to {} the {}', command_tokens[0], command_tokens[1])
    response = requests.post('localhost:5000/network/wol', data={'computer_name': target})
        
