import numpy as np
from langchain_community.embeddings import DashScopeEmbeddings


def euclidean_distance(vector1,vector2):
    """计算欧式距离"""
    return np.linalg.norm(np.array(vector1)-np.array(vector2))

if __name__ == '__main__':
    texts = ["今天天晴", "今天下雨", "小猫很可爱"]

    embedding = DashScopeEmbeddings()

    vectors = embedding.embed_documents(texts)

    #计算欧式距离
    print(f"'{texts[0]}'与'{texts[1]}'的欧式距离: {euclidean_distance(vectors[0], vectors[1])}")
    print(f"'{texts[1]}'与'{texts[2]}'的欧式距离: {euclidean_distance(vectors[1], vectors[2])}")
    print(f"'{texts[0]}'与'{texts[2]}'的欧式距离: {euclidean_distance(vectors[0], vectors[2])}")