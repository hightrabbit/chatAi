#pdf文件加载
from langchain_community.document_loaders import PyMuPDFLoader

#文件路径
file_path = "/Users/zhoujunlin/Documents/PythonProject/rag-practice/data/file/sample_document.pdf"


#创建文件加载器
loader = PyMuPDFLoader(file_path = file_path)
#加载文件
docs = loader.load()

#输出内容
# print(type(docs))
# print(type(docs[0]))

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)


