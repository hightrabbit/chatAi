from langchain_community.llms.tongyi import Tongyi

#1.创建模型客户端对象
# llm = Tongyi(model="qwen-max",api_key="")
llm = Tongyi(model="qwen-max")

#2.调用大模型
result = llm.invoke(input="你是谁？")

#处理输出结果
print(type(result))
print(result)