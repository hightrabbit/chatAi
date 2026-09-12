from langchain_community.chat_models import ChatTongyi
from langchain_community.llms.tongyi import Tongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "请解析下{aaa}的概念"
)

llm = ChatTongyi(
    model="qwen-max",
    streaming=True
)

parser = StrOutputParser()
chain = prompt_template | llm | parser

result = chain.invoke(input={"aaa":"Langchain"})
print(type(result))
print(result)