from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("markdown.txt", "r") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = splitter.create_documents([text])
print(documents)