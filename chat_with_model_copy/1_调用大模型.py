import os
from openai import OpenAI

#1.创建【模型】客户端对象
client = OpenAI(
    # SDK 默认读 OPENAI_API_KEY；百炼要用 DASHSCOPE_API_KEY，必须显式传入
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

#2.调用模型 5c
completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ]
)

#3.打印输出
print(completion.model_dump_json())

#3.1打印指定输出内容
print(completion.choices[0].message.content)