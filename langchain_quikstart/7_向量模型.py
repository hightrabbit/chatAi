from langchain_community.embeddings import DashScopeEmbeddings

#1.构建向量模型对象
embedding = DashScopeEmbeddings()

#2.向量化文本
# text = "今天天气怎么样？"
# vector = embedding.embed_query(text)

#多文本
texts = ["今天天晴","今天下雨","今天多云"]
vectors = embedding.embed_documents(texts)

#3.处理输出
# print(vector)
print(len(vectors))
print(vectors)