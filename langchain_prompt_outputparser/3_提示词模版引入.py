from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

# 1.创建模型的客户端
llm = Tongyi(model="qwen-max")

#2.提示词模版的创建
prompt_template = PromptTemplate.from_template(
    "假设你是一个{expert}专家，请你解释一下{content}是什么。"
)

#3.为提示词模版赋值
prompt = prompt_template.format(expert="AI", content="Langgraph")

#4.调用大模型
result = llm.stream(prompt)

#5.处理输出结果
for chunk in result:
    print(chunk,end="",flush=True)

