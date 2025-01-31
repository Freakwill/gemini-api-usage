#!/usr/bin/env python3

import google.generativeai as genai


# Set API Key on https://aistudio.google.com/app/apikey
API_KEY = "AIzaSyApwghFN31zbE25qQz_tlFr7DGiP2van8s"
genai.configure(api_key=API_KEY)

# export GEMINI_API_KEY=<API_KEY> in `.bashrc` or `.zshrc`

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="myclient.json"


# to see the list of supported models
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)


# print('# select a model')
# model = genai.GenerativeModel("gemini-1.5-flash")

# print('# pass a prompt string to the model')
# response = model.generate_content("what is google's gemini?")
# print('# show the response:')
# print(response.text)


# for _ in response.candidates:
#     print(_)