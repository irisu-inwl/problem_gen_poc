import logging
from random import randint
from typing import List, Optional

from sympy import (
    latex,
    symbols
)
import streamlit as st
from logic.problem_generate import (
    define_variable,
    define_constant,
)


def state_change_problem(problem_id: str):
    if st.session_state["select_problem"] != problem_id:
        st.session_state["select_problem"] = problem_id
        st.session_state["init_problem"] = False


# def setting_answer(answer_option: dict, constants: dict):

def draw_answer(answer_option: dict, answer_state: Optional[bool], symbol_dict: dict):
    print(symbol_dict)
    for left, right in symbol_dict.items():
        exec(f"{left}=right")
    # answer input
    var_name = answer_option["var_name"]
    var_answer = f'{var_name}_answer'

    command = f'{var_answer} = st.number_input("{var_name}=", key="{var_answer}")'
    exec(command)

    # answer check
    if answer_state is True:
        # ここでconstantsのlocal varが無いのでエラー
        answer = answer_option["answer"]
        answer_check = eval(f"{var_answer}=={answer}")
        if answer_check is True:
            st.write("👌")
        else:
            st.write("🙅‍♀️")


def view(
    problem_id: str, 
    vars: list, 
    constant_infos: List[dict],
    problem_text: str,
    answer_info: List[dict],
):
    state_change_problem(problem_id)

    # setting symbolic variables
    symbolic_vars = define_variable(vars)
    exec(
        f'{",".join(vars)} = symbolic_vars'
    )
    if type(symbolic_vars) is not tuple:
        symbol_dict = {vars[0]: symbolic_vars}
    else:
        symbol_dict = {var:symbol for var, symbol in zip(vars, symbolic_vars)}
    constant_names = list(map(lambda x: x["var_name"], constant_infos))
    constant_labels = ",".join(constant_names)
    
    # setting constant value
    if st.session_state["init_problem"] is False:
        logging.info(constant_infos)
        constants = define_constant(constant_infos)
        exec(
            f'{constant_labels} = constants'
        )
        
        for var_name in constant_names:
            exec(f'st.session_state["{var_name}"]={var_name}')
        st.session_state[f'init_{problem_id}'] = True
    else:
        for var_name in constant_names:
            exec(f'{var_name} = st.session_state["{var_name}"]')
    
    symbol_dict.update(
        { var_name: st.session_state[var_name]  for var_name in constant_names }
    )

    # write problem text
    problem_text = eval(f'f"{problem_text}"')
    st.write(problem_text)

    # answer 
    answer_options = answer_info["answer_options"]
    answer_text = answer_info["text"]
    st.write(answer_text)

    answer_option_container = st.container()
    answer_button_container = st.container()

    with answer_button_container:
        answer_button = st.button("Answer")

    with answer_option_container:
        for answer_option in answer_options:
            draw_answer(answer_option, answer_button, symbol_dict)

    st.button("別の問題を解く")