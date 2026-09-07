from openai import OpenAI
import os

def get_response():
    client = OpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen3.8-max",
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': '你是谁？'}],
        #流式输出开启
        stream=True,
        #开启打印token消耗，在最后一个thunk里面
        stream_options={"include_usage": True}
        )
    for chunk in completion:
        if chunk.choices:
            reply = chunk.choices[0].delta.content
            if reply :
                print(reply,end = "",flush=True)
        elif hasattr(chunk,"usage") and chunk.usage:
            print(f"token使用情况:{chunk.usage}")

if __name__ == '__main__':
    get_response()