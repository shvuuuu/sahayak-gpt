from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, GPTListIndex

def search(query):
    documents = SimpleDirectoryReader('data').load_data()
    
    index = GPTVectorStoreIndex.from_documents(documents)
    
    query_engine = index.as_query_engine()
    
    response = query_engine.query(query)
    
    return response