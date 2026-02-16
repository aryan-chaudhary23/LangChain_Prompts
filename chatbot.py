from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = OllamaLLM(
    model="llama3",      
    temperature=0.7
)

chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))

    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")
print(chat_history)