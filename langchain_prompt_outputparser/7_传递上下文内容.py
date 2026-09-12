from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#1.定义聊天提示词模版
chat_prompt_template = ChatPromptTemplate([
        ("system", "假设你是一个AI专家"),
        #历史聊天记录
        MessagesPlaceholder("history"),
        ("human", "我刚才问了什么内容？")
])

#2.定义历史聊天记录存放的集合
history_chat = [
    ("human", "什么是Langgraph"),
    ("ai", "Langgraph是一种将自然语言处理（NLP）与图数据结构相结合的技术或方法。")
]

#3.调用模型将历史记录填充到模版里-3中方法
#方法一
# chat_prompt_template = chat_prompt_template.format(history = history_chat)

#方法二
# chat_prompt_template = chat_prompt_template.invoke(input={"history":history_chat})

#方法三

#创建模型客户端
llm = Tongyi(model="qwen-max")

#创建lcel表达式
chain = chat_prompt_template | llm

#调用大模型
result = chain.stream(
    input={"history":history_chat},
)
#处理输出结果
print(type(result))
for chunk in result:
    print(chunk,end="",flush=True)
