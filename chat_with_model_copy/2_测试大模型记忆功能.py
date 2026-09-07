import os
from openai import OpenAI

client = OpenAI(
    # SDK 默认读 OPENAI_API_KEY；百炼要用 DASHSCOPE_API_KEY
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好，我是周俊霖"},
    ]
)
print("第一次调用：")
print(completion.choices[0].message.content)

completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role": "user", "content": "我是谁？"},
    ]
)
print("第二次调用：")
print(completion.choices[0].message.content)