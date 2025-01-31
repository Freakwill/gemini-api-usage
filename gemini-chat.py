#!/usr/bin/env python3

import google.generativeai as genai

import pathlib
import yaml
file = pathlib.Path('history.yaml')

# Set API Key on https://aistudio.google.com/app/apikey
GEMINI_API_KEY = "AIzaSyApwghFN31zbE25qQz_tlFr7DGiP2van8s"
genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")  #Initialize the chat
chat = model.start_chat(history=[])

while True:
    message = input("User: ")  # such as "What is the meaning of the life?"
    
    if message == 'quit':
        break
    elif message == 'clear':
        chat.history = []
    elif message == 'restart':
        chat = model.start_chat(history=[])
    elif message == 'save':
        if file.exists():
            print("The avaiable history file will be covered!")
        file.write_text(yaml.dump(chat.history, allow_unicode=True))
    elif message == 'load':
        file = pathlib.Path('history.yaml')
        if file.exists():
            chat.history = yaml.safe_load(str(file))
        else:
            print('No history is loaded!')
    response = chat.send_message(message)

    print("Model: ", response.text)

print('The chat has ended.')


