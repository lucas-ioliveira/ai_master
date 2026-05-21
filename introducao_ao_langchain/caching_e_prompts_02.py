from langchain_community.llms import Ollama
from langchain_community.cache import InMemoryCache # Cache na memoria ram, enquanto a aplicação estiver on
from langchain_community.cache import SQLiteCache # Cache persistente
from langchain.globals import set_llm_cache # Config para usar o cache

# Para cache na memoria ram
set_llm_cache(InMemoryCache())

# Para cache em banco
set_llm_cache(
    SQLiteCache(database_path='ollama_cache.db')
)

model = Ollama(model='qwen3.5:9b')

prompt = 'Quem foi Alan Turing?'

response = model.invoke(prompt)
print(f'Chamada 01: {response}')

print()

response_02 = model.invoke(prompt)
print(f'Chamada 02: {response_02}')