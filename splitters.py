from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import load_csv as lc

# 此python檔用來確認text chunk 切割的狀況

file_path = lc.output_file
chunk_size = 900
chunk_overlap = 180

def load_and_split_documents(file_path, chunk_size=500, chunk_overlap=100):
    try:
        loader = TextLoader(file_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        split_documents = text_splitter.split_documents(documents)
        return split_documents
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_first_documents(documents, first_chunks=1):
    print("Number of all text chunks:", len(documents),"\n")
    print("The first",first_chunks,"chunk content:","\n")
    for i in range(min(first_chunks, len(documents))):
        print(documents[i])
        print("\n")

# 可調整load_and_split_documents 函數的chunk size與 chunk overlap
if __name__ == "__main__":
    docs = load_and_split_documents(file_path, chunk_size, chunk_overlap)
    print_first_documents(docs)
    print("chunk_size:", chunk_size,"\n")
    print("chunk_overlap:", chunk_overlap,"\n")