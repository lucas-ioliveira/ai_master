from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate


model = ChatOllama(model='qwen3.5:9b')

template = '''
Traduza o texto do {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.from_template(template)
prompt = prompt_template.format(
    idioma1='Português',
    idioma2='Francês',
    texto='Boa tarde.'
)

print(f'Prompt: {prompt}')

response = model.invoke(prompt)
print(f'Response: {response}')
