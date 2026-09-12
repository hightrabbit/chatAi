from typing import Any

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field



#结构化输出

class IntentResult(BaseModel):
    intents : list[str] = Field(description = "意图列表，每个元素为一个意图名称")
    slots: dict[str, Any] = Field(description="slots值字典，键为slots名称，值为slots值")
    score: float = Field(description="置信度分数，取值范围0-1，越大表示越确信该意图")


class IntentRecognizer:
    """
    意图识别器：通过大语言模型识别用户输入的意图，输出IntentResult对象
    """

    def __init__(self, llm: ChatTongyi):
        """"""
        # chain  = prompt | llm | outputparse

        self.__prompt = ChatPromptTemplate.from_messages([
            {"system","系统提示词"},
            #上下文和用户输入
            {"ai","上下文内容:{chat_history}"},
            ("human","用户输入:{user_input}")
        ])

        #让大模型输出结构化
        self.__llm = llm.with_structured_output(IntentResult)
        self.__chain = self.__prompt | self.__llm

    #意图识别方法
    def recongnize(self,user_input: str,chat_history:str | None = None) -> IntentResult:
        # 1.调用llm去识别用户的意图，输出str格式的json字符串
        chat_history = chat_history if chat_history else ""
        result = self.__llm.invoke(input={"chat_history":chat_history,"user_input":user_input})

        #3.返回结果
        if result is None:
            return IntentResult(
                intents=["general"],
                slots={},
                score=0.0,
            )
        return result


