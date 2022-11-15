import logging
from random import randint

from sympy import (
    latex,
    symbols
)
import streamlit as st

from logic.problem_generate import define_variable
from data.problems import problem_data
from views.problems import view as problem_view


# init state
if "init_problem" not in st.session_state:
    st.session_state["init_problem"] = False

if "select_problem" not in st.session_state:
    st.session_state["select_problem"] = None

units = problem_data["units"]

options = [
    {
        "unit_key": unit_key,
        "subunit_key": subunit_key,
        "title": f'{unit_value["name"]}_{subunit_value["name"]}'
    } 
    for unit_key, unit_value in problem_data["units"].items()
    for subunit_key, subunit_value in unit_value["subunits"].items()
]

choice_problem = st.sidebar.radio(
    "Problem List", options, format_func=lambda x: x["title"]
)

if choice_problem is not None:
    unit_key = choice_problem["unit_key"]
    subunit_key = choice_problem["subunit_key"]
    problem_config = problem_data["units"][unit_key]["subunits"][subunit_key]
    problem_id = f'{unit_key}_{subunit_key}'
    vars = problem_config["vars"]
    constant_infos = problem_config["constants"]
    problem_text = problem_config["problem_text"]
    answer_info = problem_config["answer_info"]
    problem_view(
        problem_id,
        vars,
        constant_infos,
        problem_text,
        answer_info
    )