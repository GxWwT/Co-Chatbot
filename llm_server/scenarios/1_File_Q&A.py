from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.fake import FakeEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

loader = TextLoader("Readme.md")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = FakeEmbeddings(size=1504)
docsearch = Chroma.from_documents(texts, embeddings)


qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    return_source_documents=True,
)

# 基于本地知识问答的提示词模版
PROMPT_TEMPLATE = """【指令】根据已知信息，简洁和专业的来回答问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题”，不允许在答案中添加编造成分，答案请使用中文。 

【已知信息】{context} 

【问题】{question}"""