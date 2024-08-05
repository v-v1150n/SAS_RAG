import asyncio
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from nemoguardrails import RailsConfig
from nemoguardrails.integrations.langchain.runnable_rails import RunnableRails
import vectorstore as vs

#此python檔用來將向量庫與LLM連結並加上Guardrail

load_path = './Vector_db/all_data' # Vector data base path
# load_path = './Vector_db/chem_data'
def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

# 建立RAG Chain 選擇llm model, embedding model, vector database
def chain(llm_model='llama3', embedding_model='all-MiniLM-L12-v2', load_path=load_path):
    llm = ChatOllama(model=llm_model, temperature=0)
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    db_load = Chroma(persist_directory=load_path, embedding_function=embeddings)
    retriever = db_load.as_retriever()
    
    template = """
    你是一個回答問題的助手也是化學領域專家
    依據上下文的內容context: {context}
    回答使用者提出的問題Question: {question}
    如果不知道就回答不知道，不要生成無關的答案
    只使用繁體中文回答問題
    """
    prompt = ChatPromptTemplate.from_template(template)

    config = RailsConfig.from_path("./config")
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    guardrails = RunnableRails(config)
    chain_with_guardrails = guardrails | chain
    
    return chain_with_guardrails

if __name__ == "__main__":
    my_chain = chain()