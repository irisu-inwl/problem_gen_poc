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
                        "text": "答え: $x=\\frac{{-B\pm\sqrt{{C}}}}{{A}}$",
                        "answer_options": [
                            {
                                "var_name": "A",
                                "answer": "2*a",
                            },
                            {
                                "var_name": "B",
                                "answer": "b",
                            },
                            {
                                "var_name": "C",
                                "answer": "b**2-4*a*c",
                            },
                        ]
                    }
                }
            }
        }
    }
}

