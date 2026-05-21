# Exemplo básico de como consumir o LLM

from langchain_ollama.llms import OllamaLLM


model = OllamaLLM(model='qwen3.5:9b')

messages = [
    {'role':'system', 'content':'Você é um assistente que fornece informações sobre figuras históricas'},
    {'role':'user', 'content':'Quem foi Alan Turing?'}
]

response = model.invoke(messages)
print(f'Response:{response}')
