from latexSym import symbols_in_latex

def equation(LHS, Operand, RHS):
    return f"{LHS} {Operand} {RHS}"


def convert_symbol_to_latex(symbol_list):
    result_string = ""

    for element in symbol_list:
        if element in symbols_in_latex:
            result_string += symbols_in_latex[element] + " "
        else:
            print(f"{element} Character Not found")

    print(result_string)

convert_symbol_to_latex(["$", ">", "<=", ";", "Σ"])