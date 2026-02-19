from .vectorstore import build_vectorstore

def get_retriever(file_path: str):
    vectorstore = build_vectorstore(file_path)
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4}
        )

