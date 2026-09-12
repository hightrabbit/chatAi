#1.准备示例数据
from sys import prefix

from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

examples = [
    {"input": "高兴", "output": "愉悦"},
    {"input": "快速", "output": "迅猛"},
    {"input": "美丽", "output": "绚丽"}
]
#2.构建提示词模版
prompt_template = PromptTemplate.from_template(
    template="输入：{input}\n输出：{output}"
)

#3.创建fewShotPromptTemplate
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_template,
    prefix="请根据以下示例，将输入词语转换为同义词",
    suffix="基于示例回答问题。用户输入：{word}\n输出：",
    input_variables=["word"]
)

#4.调用
prompt_text = few_shot_prompt_template.format(word = "悲伤")

#5.创建模型客户端
llm = Tongyi(model="qwen-max")

#6.调用大模型
result = llm.invoke(input=prompt_text)

#7.处理输出结果
print(type(result))
print(result)