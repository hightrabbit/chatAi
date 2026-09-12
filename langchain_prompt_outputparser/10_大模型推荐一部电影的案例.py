from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate

#构建提示词模版
prompt = PromptTemplate.from_template(
"请根据以下描述，提取书籍信息并以JSON格式输出。\n"
    "描述：{description}\n"
    "输出格式：{{\"title\": \"书名\", \"author\": \"作者\", \"year\": 出版年份}}"
)


#创建模型客户端
llm = ChatTongyi(
    model="qwen-max"
)

#构建json解释器
parser = JsonOutputParser()

#lcel表达式构建
chain = prompt | llm | parser

#调用大模型输出结果
result = chain.invoke(input={"description":"《三体》是刘慈欣创作的科幻小说，于2008年首次出版。"})

#处理大模型返回结果
print(type(result))
print(result)
