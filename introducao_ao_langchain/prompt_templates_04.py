from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model='qwen3.5:9b')

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='Você deve responder baseado em dados geográficos de regiões do Brasil.'),
        HumanMessagePromptTemplate.from_template('Me fale sobre a região {regiao}.'),
        AIMessage('Claro, vou começar coletando informações sobre a região e analisando os dados disponíveis.'),
        HumanMessage(content='Certifique-se de incluir dados demográficos.'),
        AIMessage(content='Entendido. Aqui estão os dados:')
    ]
)

prompt = chat_template.format(regiao='Suldeste')

response = model.invoke(prompt)
print(f'Response: {response.content}')
