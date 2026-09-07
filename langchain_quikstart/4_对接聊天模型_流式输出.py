from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage

#1.创建模型客户端
llm = ChatTongyi(model="qwen3-max",streaming=True)

#2.准备消息上下文
chat_history = [
    SystemMessage(content="背景设定，你是一名数学老师"),
    HumanMessage(content="你是谁？")
]

#3.将准备好的上下文发送给大模型
result = llm.stream(input=chat_history)

#4.处理返回结果
for chunk in result:
    print(chunk.content,end="",flush=True)