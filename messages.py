from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3",      
    temperature=0.7
)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = llm.invoke(messages)
#print(result)

messages.append(AIMessage(content=str(result)))

print(messages)