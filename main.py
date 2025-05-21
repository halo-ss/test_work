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
df = pd.read_csv("freelancer_earnings_bd.csv")
input_text = input("Введите запрос:")
code_block = check_table_bot(input_text)
# print(code_block)
exec(code_block)  
user_question = f"""
таблица: {df_result.to_string(index=False)}
запрос: {input_text}
"""
result_bot(user_question)
print(df_result)
