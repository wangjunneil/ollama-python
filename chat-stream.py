import ollama

messages = [
    {
        'role': 'user',
        'content': '金融中期货是什么概念'
    }
]

for part in ollama.chat('llama2-chinese', messages=messages, stream=True):
    print(part['message']['content'], end='', flush=True)

print()