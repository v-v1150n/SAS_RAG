import os
import time
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
import load_csv as lc
import splitters as sp

# 此python檔用來將切割後的txt檔存為vector store

output_path = './Vector_db/chem_data'

# 存為vector database
def save_to_chroma(docs, embeddings, output_path):
    try:
        db_store = Chroma.from_documents(docs, embeddings, persist_directory=output_path)
        print(f"db_store successfully saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

def main():

    start_time = time.time()

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    doc1 = sp.load_and_split_documents(lc.output_file, 900, 180)

    save_to_chroma(doc1, embeddings, output_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Script executed in {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()