from latexSym import symbols_in_latex

def equation(LHS, Operand, RHS):
    return f"{LHS} {Operand} {RHS}"


def convert_symbol_to_latex(symbol_list):
    result_string = ''
    for element in symbol_list:
        try:
            result_string += symbols_in_latex[element]
        except:
            print(f"{element} Character Not found")
    print(result_string)
            