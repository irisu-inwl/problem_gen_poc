import logging
from random import randint
from typing import List
import re

from sympy import (
    latex,
    symbols,
    sqrt,
)
import streamlit as st

def define_variable(vars: list):
    logging.info(
        f'{",".join(vars)} = symbols("{" ".join(vars)}")'
    )
    return eval(f'symbols("{" ".join(vars)}")')


def define_constant(constant_infos: List[dict]):
    constants = [
        eval( '{method}(**{kwargs})'.format(**constant_info) ) 
        for constant_info in constant_infos
    ]

    return constants

def answer_generate(answer: str, symbol_dict: dict, answer_option: dict = {}):
    # print(symbol_dict)
    for left, right in symbol_dict.items():
        exec(f"{left}=right")
    
    exp = eval(answer)
    exp_text = latex(exp)
    # ダブりありダブりなしで分岐させてもよい
    # 今はダブったもの全部同じ記号にしている
    numbers = set(re.findall(f"([0-9]+)", exp_text)) - set(answer_option.values())
    if len(numbers) > 0:
        answer_option.update(
            {
                chr(ord('A') + len(answer_option) + idx): num
                for idx, num in enumerate(numbers)
            }
        )
    
    for answer_char, answer_value in answer_option.items():
        exp_text = re.sub(answer_value, answer_char, exp_text)

    return answer_option, exp_text
