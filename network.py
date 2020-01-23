import request

def handle_command(command_tokens):
    switcher={
        "wake":wake_command
    }
    
    switcher.get(command_tokens[0], 

def invalid_command(command_string):
    print("I'm sorry Reclaimer, but {} isn't a support subroutine for the Network module yet", command_string)

def wake_command(target):
        
