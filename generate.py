import ollama

response = ollama.generate('llama2-chinese', '金融中期货是什么概念')
print(response['response'])