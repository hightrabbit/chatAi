from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

#1.创建文件消息存储对象--需要传入文件路径
file_memory = FileChatMessageHistory("contant.txt")

#2.存消息
file_memory.add_message(HumanMessage("你好"))
file_memory.add_message(AIMessage("你也好"))
#3.获取消息

print(file_memory.messages)