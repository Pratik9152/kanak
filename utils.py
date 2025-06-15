import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load OpenRouter API key from environment variable
openai_key = os.getenv("OPENAI_API_KEY")

# Load vectorstore or recreate it
VECTORSTORE_PATH = "vectorstore"

def load_vectorstore():
    pdf_files = [f for f in os.listdir(VECTORSTORE_PATH) if f.endswith(".pdf")]
    if not pdf_files:
        raise FileNotFoundError("No policy PDF found in vectorstore.")

    docs = []
    for pdf in pdf_files:
        loader = PyPDFLoader(os.path.join(VECTORSTORE_PATH, pdf))
        docs.extend(loader.load())

    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# Initialize chatbot
retriever = load_vectorstore().as_retriever()
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.3)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def get_answer(query):
    result = qa_chain(query)
    answer = result['result']

    # Add references if available
    sources = result.get('source_documents', [])
    if sources:
        refs = "\n\n\ud83d\udcce **References:**\n"
        for i, doc in enumerate(sources[:3], start=1):
            refs += f"{i}. Page {doc.metadata.get('page', '?')}, File: {doc.metadata.get('source', '?')}\n"
        answer += refs

    return answer
