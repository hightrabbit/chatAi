from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

#1.创建模型客户端
llm = Tongyi(model="qwen-max")

#2.创建提示词模版
prompt_template = PromptTemplate.from_template(
     "假设你是一个{expert}专家，请你解释一下{content}是什么。"
)

#3.LCEL表达式
chain = prompt_template | llm #前一个组件的输出是后一个组件的输入

#4.调用大模型
result = chain.stream(input={"expert":"AI","content":"Langgraph"})

#处理输出结果
print(type(result))
for chunk in result:
    print(chunk,end="",flush=True)
