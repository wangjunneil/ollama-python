import ollama

for part in ollama.generate('llama2-chinese', '金融中期货是什么概念', stream=True):
    print(part['response'], end='', flush=True)