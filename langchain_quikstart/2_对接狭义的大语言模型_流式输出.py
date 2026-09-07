from langchain_community.llms.tongyi import Tongyi

#1.创建模型客户端对象
# llm = Tongyi(model="qwen-max",api_key="")
llm = Tongyi(model="qwen-max")

#2.调用大模型
result = llm.stream(input="你是谁？")

#处理输出结果
for chunk in result:
    print(chunk,end="",flush=True)