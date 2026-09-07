from openai import OpenAI
import os


class MultiTurnChat:
    def __init__(self,model:str,base_url:str,system_prompt:str):
        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url=base_url,
        )
        self.model=model
        #对话列表
        self.chat_history=[]

        #如果系统提示词不为空，需要添加到对话列表
        if system_prompt:
            self.chat_history.append({"role":"system","content":system_prompt})

    #添加用户消息
    def add_user_message(self,content:str):
        self.chat_history.append({"role":"user","content":content})

    #添加ai回复的消息
    def add_system_message(self,content:str):
        self.chat_history.append({"role":"system","content":content})

    #调用模型发送消息
    def send(self,user_message:str):
        """发送消息"""
        #1.添加消息到历史对话
        self.add_user_message(user_message)

        #2.调用模型
        completion = self.client.chat.completions.create(
            model=self.model,
            messages= self.chat_history
        )

        #3.提取模型回复的结果
        reply = completion.choices[0].message.content

        #4.添加模型对话到历史对话列表
        self.chat_history.append({"role":"assistant","content":reply})
        return reply



if __name__ == '__main__':
    """开始调用"""
    #1.配置参数
    BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    MODULE = "qwen3.8-max"
    SYSTEM_PROMPT = "背景设定，你现在是一名AI老师，负责教学AI课"

    #2.创建多轮对话对象
    chat = MultiTurnChat(
        base_url=BASE_URL,
        system_prompt = SYSTEM_PROMPT,
        model = MODULE,
    )

    print("多轮对话已经启动，输入内容后回车发送。输入:'exit'或'quit'退出程序。\n")

    #3.循环接受用户输入并且回答
    while True:
        """"""
        # 获取用户输入
        user_input = input("用户:")
        if user_input in ["exit","quit"]:
            print("对话结束")
            break
        #跳过空的输入
        if not user_input.strip():
            print("请勿输入空白字符")
            continue
        reply = chat.send(user_input)

        print(f"ai老师:{reply}")
