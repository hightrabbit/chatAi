from typing import Dict, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 存储每个对话的历史消息：key是chat_session_id，value是会话历史记录
_session_store: Dict[str, BaseChatMessageHistory] = {}

#1.准备历史消息类
class Memory:
    #准备session_id对应的历史消息记录
    def get_session_history(self,session_id:str) -> BaseChatMessageHistory:
        if session_id not in _session_store:
            _session_store[session_id] = InMemoryChatMessageHistory()
        return _session_store[session_id]

    #添加人类消息
    def add_human_message(self,session_id:str,message:str |HumanMessage) -> None:
        chat_history =  self.get_session_history(session_id)
        if isinstance(message,str):
            chat_history.add_message(HumanMessage(message))
        else:
            chat_history.add_message(message)
    #添加ai消息
    def add_ai_message(self,session_id:str,message:str |AIMessage) -> None:
        chat_history =  self.get_session_history(session_id)
        if isinstance(message,str):
            chat_history.add_message(AIMessage(message))
        else:
            chat_history.add_message(message)

    #查询当前id下的历史消息
    def get_messages(self,session_id:str) -> List[BaseMessage]:
        return self.get_session_history(session_id).messages

#2.创建会话类
class ChatSession:
    def __init__(self, session_id: str, system_prompt:str = "你是一个ai助手") -> None:
        self.session_id = session_id
        self.memory = Memory()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{user_input}")
        ])
        self.model = ChatTongyi(model="qwen3-max", streaming=True)
        self.parser = StrOutputParser()
        self.chain = self.prompt | self.model | self.parser

    def send(self, user_input: str) -> None:
        # 获取当前id下的全部历史会话
        chat_history = self.memory.get_messages(self.session_id)
        # 发送消息给大模型
        stream = self.chain.stream(input={
            "chat_history": chat_history,
            "user_input": user_input
        })

        # 处理返回结果
        full_reply = ""
        for chunk in stream:
            full_reply += chunk
            yield full_reply

        # 把用户消息和模型消息都存到当前历史会话里
        self.memory.add_human_message(self.session_id, full_reply)
        self.memory.add_ai_message(self.session_id, full_reply)




# ========== 测试代码 ==========
if __name__ == "__main__":
    session = ChatSession("user_001")

    print("用户: 你好，我叫阿苑")
    print("AI: ", end='', flush=True)
    for chunk in session.send("你好，我叫阿苑"):
        print(chunk, end='', flush=True)
    print()

    print("用户: 我叫什么名字？")
    print("AI: ", end='', flush=True)
    for chunk in session.send("我叫什么名字？"):
        print(chunk, end='', flush=True)
    print()