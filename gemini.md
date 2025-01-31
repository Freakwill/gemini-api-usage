# Exploring the Usage of Google's Gemini API

Google's Gemini API is a powerful tool for developers looking to incorporate advanced natural language understanding and generation capabilities into their applications. This report explores the usage of the Gemini API, detailing its functionality, benefits, and potential applications. Through examples and tutorials, we aim to provide a comprehensive guide for developers interested in leveraging this cutting-edge AI technology.

Report: William Song


Keywords: Google Gemini, AI Integration

Tools: Python, Colab



Time: 2025/1/22: pm3:00-4:00

Venue: A3-312

zoom3





## 1. Requirement

### Install

`pip install -q google-generativeai`

### get API key

1. open url `https://aistudio.google.com/prompts/`
2. press [Get API key]
3. copy the key

### get `GOOGLE_APPLICATION_CREDENTIALS`

-  access `https://console.cloud.google.com/iam-admin`

  - Create a service account in your *Google Cloud project* with the necessary permissions (at least `GenAI User` role).
  - Download the service account key file (JSON).
  - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file. This tells the library where to find your credentials.

## 2. Test

```python
import google.generativeai as genai

# Set API Key on https://aistudio.google.com/app/apikey
GEMINI_API_KEY = "AIzaSyApwghFN31zbE25qQz_tlFr7DGiP2van8s"
genai.configure(api_key=GEMINI_API_KEY)  # .bashrc / .zshrc

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="myclient.json"

# to see the list of supported models
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
```



## 3. models and `generate_content` method

```python
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is the most import thing in the life?")
print(response.text)

# candidates: multiple possible responses for a single prompt
for _ in response.candidates:
    print(_)
```



`response = model.generate_content("Does life really have meaning?", stream=True)`



## 4. Chat with the Gemini

### `send_message` method

```python
model = genai.GenerativeModel("gemini-1.5-flash")  #Initialize the chat
chat = model.start_chat(history=[])
response = chat.send_message("What is the meaning of the life from the view of evolution theory?")
print(response.text)

# dialogue with `while` looping
while True:
    message = input("User: ")  # such as "What is the meaning of the life from the view of evolution theory?"
    if message == 'quit': break
    response = chat.send_message(message)
    print("Model: ", response.text)
```

### show the history

```python
for message in chat.history:
    if message.role == 'model':
        print('==========================')
    display(to_markdown(f"**{message.role}**: {message.parts[0].text}"))
```

