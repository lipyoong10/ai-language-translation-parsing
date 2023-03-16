#Import open AI OS and System Modules

import openai
import gradio as gr

openai.api_key = 'platform openai api_key'

messages = [
    {"role": "system", "content": "Educational language parser and translator"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": "Please translate for each phrase in this sentence into English phrase by phrase, and explain the sentence later as a whole. Specifically identify the term and the pronunciation of the phrase as well \n\n"+input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.components.Textbox(lines=30, label="Paste your sentence here (4000 character limit)") #Limit of 4000 chars
outputs = gr.components.Textbox(lines=30, label="AI translation and parsing output")

demo = gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Grammar Checker",
             description="AI translator and parser (Slowness due to smaller server)",
             theme=gr.themes.Base(), css="footer {visibility: hidden}").launch(server_name="0.0.0.0",auth=("username","password"))

