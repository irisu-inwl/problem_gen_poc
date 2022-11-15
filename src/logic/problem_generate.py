import logging
from random import randint
from typing import List

from sympy import (
    latex,
    symbols
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
