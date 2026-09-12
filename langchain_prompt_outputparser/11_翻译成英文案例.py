from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

model = ChatTongyi(model="qwen3-max")

# 1.生成推荐电影（JSON格式）
prompt1 = PromptTemplate.from_template(
    "根据用户喜欢的电影类型，推荐一部电影并以JSON格式输出。\n"
    "用户类型：{genre}\n"
    "输出格式：{{\"title\": \"电影名称\", \"director\": \"导演\", \"year\": 上映年份, \"reason\": \"推荐理由\"}}"
)

json_parser = JsonOutputParser()

# 2.直接使用字典中的键作为变量名
prompt2 = PromptTemplate.from_template(
    "请将以下电影推荐信息翻译成英文，只输出翻译结果。\n"
    "电影名称：{title}\n导演：{director}\n上映年份：{year}\n推荐理由：{reason}"
)

str_parser = StrOutputParser()

# 构建链：JsonOutputParser 输出的字典会自动匹配 prompt2 的变量
chain = prompt1 | model | json_parser | prompt2 | model | str_parser

result = chain.invoke({"genre": "科幻"})
print(result)