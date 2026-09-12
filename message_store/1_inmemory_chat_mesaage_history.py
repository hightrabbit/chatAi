from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

#内存管理消息

#1.创建消息存储对象
memory  = InMemoryChatMessageHistory()

#2.添加消息
memory.add_message(HumanMessage("你是谁？"))
memory.add_message(AIMessage("我是ai"))
#3.打印结果
print(memory.messages)