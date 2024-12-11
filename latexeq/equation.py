def equation(LHS, Operand, RHS):
    return f"{LHS} {Operand} {RHS}"


def convert_symbol_to_latex(symbol_list):
    result_string = ''
    for element in symbol_list:
        match element:
            case ">":
                return ""
            case ">=":
                return ""
            case "<":
                return ""
            case "<=":
                return ""
            case "=":
                return ""
            case "+":
                return ""
            case "-":
                return ""
            case "x":
                return ""
            case ".":
                return ""
            case "sigma":
                return ""
            case "integral":
                return ""
            