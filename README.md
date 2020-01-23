# MendicantBias
slackbot for interfacing slack to home automation tasks

# Configuring .env:
1. clone git repo
2. run `python3 -m venv botVenv` in project folder
3. run `source botVenv/bin/activate` in project folder
4. run `pip install -r requirements.txt` in project folder
5. create a .env file in the project root folder
6. add the following text to the .env file:
    `SLACK_BOT_TOKEN='<your slackbot auth token here>'
7. save the file
8. running `python3 mendicant_bias.py` should start the bot!
