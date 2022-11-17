problem_data = {
    "units": {
        "quadratic_function": {
            "name": "二次関数",
            "subunits": {
                "solution_fomula": {
                    "name": "解の公式",
                    "vars": ["x"],
                    "constants": [
                        {
                            "var_name": "a", 
                            "method": "randint",
                            "kwargs": {
                                "a": 1,
                                "b": 10
                            }
                        },
                        {
                            "var_name": "b", 
                            "method": "randint",
                            "kwargs": {
                                "a": 0,
                                "b": 10
                            }
                        },
                        {
                            "var_name": "c", 
                            "method": "randint",
                            "kwargs": {
                                "a": 0,
                                "b": 10
                            }
                        },
                    ],
                    "problem_text": "${latex(a*x**2+b*x+c)}$の解を求めよ。",
                    "answer_info": {
                        "type": "autogen", 
                        "answers": [
                            "(-b+sqrt(b**2-4*a*c))/(2*a)", 
                            "(-b-sqrt(b**2-4*a*c))/(2*a)", 
                        ],
                        "symmetry": True,
                        # "type": "option", # option: 選択, autogen: 正当自動生成
                        # "text": "答え: $x=\\frac{{-B\pm\sqrt{{C}}}}{{A}}$",
                        # "answer_option": {
                        #    "A": "2*a",
                        #    "B": "b",
                        #    "C": "b**2-4*a*c",
                        # },
                    }
                }
            }
        }
    }
}

