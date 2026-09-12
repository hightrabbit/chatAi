from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Dict

# 直接从子模块导入，方便 IDE 解析
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing_extensions import Any


#定义意图识别的结果
@dataclass(frozen=True) #定义的类不可改变
class IntentResult:
    intents : list[str]
    slots: dict[str, Any]
    score: float

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

        self.__llm = llm
        self.__chain = self.__prompt | self.__llm | StrOutputParser()

    #意图识别方法
    def recongnize(self,user_input: str,chat_history:str | None = None) -> IntentResult:
        # 1.调用llm去识别用户的意图，输出str格式的json字符串
        chat_history = chat_history if chat_history else ""
        result = self.__llm.invoke(input={"chat_history":chat_history,"user_input":user_input})

        # 2.解析大模型输出 --创建解析方法
        data = self.__parse_str_to_json(result)
        #2.1解析intents意图
        intents = data.get("intents")
        if not isinstance(intents, list):
            intent = data.get("intent")
            intenes = [intent] if isinstance(intent, str) else []

        #2.2 解析slots插槽
        slots= data.get("slots") if isinstance(data.get("slots"), dict) else {}

        #2.3解析confidence自信度
        try:
            confidence = float(data.get("confidence"))
        except:
            confidence = 0.0
        #约束范围
        confidence = max(0.0, min(1.0, confidence))

        #3.返回结果
        return IntentResult(intents, slots, confidence)








    def __parse_str_to_json(self,text:str)->dict[str, Any]:
        if not text or text.strip():
            return {{"intents": ["general"], "slots": {}, "confidence": 0.0}}


        #将text转换成dict
        text = text.strip()
        try:
            return json.loads(text)
        except json.decoder.JSONDecodeError:
           pass

        #如果解析失败，尝试从模型中提取json字符串
        find_text = re.search(r"{{.*?}}",text,re.DOTALL)
        if find_text:
            try:
                return json.loads(find_text.group(0))
            except json.decoder.JSONDecodeError:
                pass



