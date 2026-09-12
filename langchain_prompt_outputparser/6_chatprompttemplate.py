from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import ChatPromptTemplate

#1.创建聊天提示词模版
chat_prompt_template = ChatPromptTemplate.from_messages([
        ("system", "假设你是一个{expert}专家"),
        ("human", "什么是{user_input}")
    ])

#2.填充模版中的可变参数
#方法一
# chat_prompt_template = chat_prompt_template.format(
#     expert="AI",
#     user_input = "Langgraph"
# )
#
# print(type(chat_prompt_template))
# print(chat_prompt_template)


#方法二
# chat_prompt_template = chat_prompt_template.invoke(
#     input={
#         "expert":"AI",
#         "user_input":"Langgraph"
#            }
# )
# print(type(chat_prompt_template))
# print(chat_prompt_template.to_string())

#方法三
#3.创建模型客户端
llm = Tongyi(model="qwen-max")

#4.lcel表达式
chain = chat_prompt_template | llm

#5.调用大模型
result = chain.stream({"expert":"AI","user_input":"Langgraph"})

#6.处理输出结果
print(type(result))
for chunk in result:
    print(chunk,end="",flush=True)
