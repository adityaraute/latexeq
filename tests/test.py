import pytest
from latexeq import equation

def test_convertEquation():
    assert equation.convert_symbol_to_latex(["$", ">", "<=", ";", "Σ"]) == "\\varpi > \\leq \\Sigma"