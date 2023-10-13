import os
from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


openai_api_key = os.environ.get("openai_api_key")

Azure_llm = AzureChatOpenAI(
    openai_api_key=openai_api_key,
    openai_api_base="https://<>.openai.azure.com/",
    deployment_name="<>",
    openai_api_version="2023-05-15",
    openai_api_type="azure"
)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
        "You are a helpful assistant having a conversation with a human."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# Set `return_messages=True` to fit into the MessagesPlaceholder
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
conversation = LLMChain(
    llm=Azure_llm,
    prompt=prompt,
    memory=memory
)


if __name__ == "__main__":
    # Notice that we just pass in the `question` variables - `chat_history` gets populated by memory
    print(conversation({"question": "hi"}))
