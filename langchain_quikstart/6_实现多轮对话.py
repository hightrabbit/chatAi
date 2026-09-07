from langchain_community.chat_models.tongyi import ChatTongyi


class MultiTurnChat:
    #1.初始化模型对象
    def __init__(self,model:str,system_prompt:str = None) -> None:
        self.llm = ChatTongyi(
            model=model,
            streaming=True  # Python 布尔值必须是 True，不是 true
        )

        #2.构建历史对话列表（必须挂到 self 上，后面方法才能用）
        self.chat_history = []

        #3.判断传入的系统提示词是否为空？不为空就加入到历史对话列表里面
        if system_prompt:
            self.chat_history.append(("system",system_prompt))

    #5.构建添加用户消息到对话历史记录列表
    def add_user_message(self,user_message:str):
        if user_message:
            self.chat_history.append(("user",user_message))

    #6.构建添加大模型返回消息到对话历史记录列表
    def add_ai_message(self,ai_message:str):
        if ai_message:
            self.chat_history.append(("ai",ai_message))

    #4.发送消息给大模型
    def send(self,user_message:str):
        #4.1添加用户消息到历史消息记录表--构建添加方法
        if user_message:
            self.add_user_message(user_message)
        #4.2流式调用大模型输出
        result = self.llm.stream(input=self.chat_history)
        #4.3收集完整回复并逐块返回
        full_reply = ""
        for chunk in result:
            if chunk.content:
                full_reply += chunk.content
                yield chunk.content
        #4.4 添加模型的完整回复到历史--构建添加方法
        self.add_ai_message(full_reply)

if __name__ == '__main__':
    """"""
    #准备初始化的配置参数
    MODLE = "qwen3-max"
    SYSTEM_PROMPT = "背景设定，你是一名数学老师"

    #初始化模型对象
    chat = MultiTurnChat(
       model=MODLE,
       system_prompt=SYSTEM_PROMPT
    )

    print("多轮对话已经启动，输入内容后回车发送。输入:'exit'或'quit'退出程序。\n")

    #开始循环对话
    while True:
        #获取用户输入
        user_input = input("human:")
        if user_input:
            if user_input in ["exit","quit"]:
                print("对话结束")
                break
            if not user_input.strip():
                print("请勿输入空白字符")
                continue
            #开始调用模型
            print(f"AI老师：", end="", flush=True)
            for chunk in chat.send(user_input):
                print(chunk,end="",flush=True)
            print()
