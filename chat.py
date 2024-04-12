#!/usr/bin/env python
import ollama

messages = [
    {
        'role': 'user',
        'content': '金融中期货是什么概念',
    }
]

response = ollama.chat(model='llama2-chinese:latest', messages=messages);
if response['done']:
    print(response['message']['content'])