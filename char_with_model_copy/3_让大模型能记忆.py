from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

#初始化上下文（消息列表）
chat_history =  []

#定义对话问题
user_message_1 = "我是周俊霖"

#添加对话到上下文中
chat_history.append({"role":"user","content":user_message_1})

completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=chat_history,
)
# print(completion.choices[0].message.content)

#第二次调用
chat_history.append({"role":"assistant","content":completion.choices[0].message.content})
user_message_2 = "我是谁？"
chat_history.append({"role":"user","content":user_message_2})

completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=chat_history,
)
print(completion.choices[0].message.content)