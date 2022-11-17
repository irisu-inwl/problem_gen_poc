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
    answer_generate,
)


def _auto_gen_answer(answers: List[str], symbol_dict: dict):
    answer_option = {}

    if st.session_state["init_problem"] is False:
        texts = []
        for answer in answers:
            answer_option, text = answer_generate(answer, symbol_dict, answer_option)
            texts.append(text)
        answer_text = f'答え: ${".".join(texts)}$'
        st.session_state["answer_option"] = answer_option
        st.session_state["answer_text"] = answer_text
        logging.info(answer_option)
    else:
        answer_option = st.session_state["answer_option"]
        answer_text = st.session_state["answer_text"]
    
    return answer_option, answer_text


def state_change_problem(problem_id: str):
    if st.session_state["select_problem"] != problem_id:
        st.session_state["select_problem"] = problem_id
        st.session_state["init_problem"] = False


# def setting_answer(answer_option: dict, constants: dict):

def draw_answer(answer_key: str, answer_value: int, answer_state: Optional[bool], symbol_dict: dict):
    print(symbol_dict)
    for left, right in symbol_dict.items():
        exec(f"{left}=right")
    # answer input
    var_name = answer_key
    var_answer = f'{var_name}_answer'

    answer_input = st.number_input(f"{var_name}=", key=var_answer)

    # answer check
    if answer_state is True:
        # ここでconstantsのlocal varが無いのでエラー
        answer_check = eval(f"{answer_input}=={answer_value}")
        
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
    else:
        for var_name in constant_names:
            exec(f'{var_name} = st.session_state["{var_name}"]')
    
    symbol_dict.update(
        { var_name: st.session_state[var_name]  for var_name in constant_names }
    )

    # write problem text
    problem_text = eval(f'f"{problem_text}"')
    st.write(problem_text)

    # Answer
    # initial answer option gen 
    
    answer_type = answer_info["type"]
    if answer_type == "autogen":
        answers = answer_info["answers"]
        answer_option, answer_text = _auto_gen_answer(answers, symbol_dict)
    else:
        answer_option = answer_info["answer_options"]
        answer_text = answer_info["text"]
    
    st.write(answer_text)

    answer_option_container = st.container()
    answer_button_container = st.container()

    with answer_button_container:
        answer_button = st.button("Answer")

    with answer_option_container:
        for answer_key, answer_value in answer_option.items():
            draw_answer(answer_key, answer_value, answer_button, symbol_dict)

    if st.session_state["init_problem"] is False:
        st.session_state["init_problem"] = True

    st.button("別の問題を解く")