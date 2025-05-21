import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
# from tabulate import tabulate
import lmstudio as lms
import warnings
from cfg import PROMPT1 , PROMPT2 
warnings.filterwarnings("ignore") # ignore all warnings


# первая ступень обработки запроса

def check_table_bot(user_question):
    model = lms.llm("qwen3-14b")
    
    prompt = f"""
<think>
{PROMPT1}

Вопрос: {user_question}
</think>
    """

    result = model.respond(prompt)
    result_str = str(result)
    code_block = result_str.split("</think>")[1]
    
    return code_block
# вторая ступень обработки вопроса вывод результата на экран
def result_bot(user_question):
    model = lms.llm("qwen3-14b")
    
    prompt = f"""
<think>
{PROMPT2}
Вопрос: {user_question}
</think>
    """

    result = model.respond(prompt)
    result_str = str(result)
    code_block = result_str.split("</think>")[1]
    
    return print(code_block)

#чтение базы
df = pd.read_csv("freelancer_earnings_bd.csv")

# получение текста
input_text = input("Введите запрос:")

# получение таблицы 
code_block = check_table_bot(input_text)
# print(code_block)

# Компиляция 
exec(code_block)
# Объединение таблицы и запроса   
user_question = f"""
таблица: {df_result.to_string(index=False)}
запрос: {input_text}
"""
#вывод результатов
result_bot(user_question)
print(df_result)
