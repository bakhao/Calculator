import math


# Fonction qui permet de parser un string et d'effectuer l'operation
def calculate(s: str):
    actual_number = 0
    current_operand = "+"
    list_of_operators = ['-', '*', "/", '+', '^']
    list_of_digit = []
    result = 0
    for i in range(len(s)):
        if s[i].isdigit():
            actual_number = int(s[i]) + actual_number * 10
        if s[i] in list_of_operators or i == len(s) - 1:
            if current_operand == "+":
                list_of_digit.append(actual_number)
            elif current_operand == "-":
                list_of_digit.append(-actual_number)
            elif current_operand == "-" and s[i - 1] == "-":
                list_of_digit.append(actual_number)
            elif current_operand == "*":
                list_of_digit[-1] = (list_of_digit[-1]) * actual_number
            elif current_operand == "/":
                list_of_digit[-1] = (list_of_digit[-1]) / actual_number
            elif current_operand == '^':
                list_of_digit[-1] = list_of_digit[-1] ** actual_number
            current_operand = s[i]
            actual_number = 0
    if s[0] == "s":
        for i in s:
            if i.isdigit():
                result = math.sqrt(int(i))
    else:
        result = sum(list_of_digit)
    return result
