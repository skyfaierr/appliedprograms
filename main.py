import re

def is_valid_math_expression(expression):
    # Регулярное выражение для проверки синтаксиса математического выражения
    pattern = re.compile(r'^[0-9a-zA-Z]+\s*([()+\-*/%=]\s*[0-9a-zA-Z]+\s*)*$')

    # Проверяем, соответствует ли выражение заданному паттерну
    if re.match(pattern, expression):
        # Проверка на правильное распределение скобок
        stack = []
        for char in expression:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False  # Закрывающая скобка без соответствующей открывающей или несовпадение типов скобок

        return not stack  # Проверяем, что все открывающие скобки имеют соответствующие закрывающие
    else:
        return False


valid_expression1 = "17*4+x-54=y"
valid_expression2 = "2+2"
valid_expression3 = "18-41*c"
valid_expression4 = "3x+2"
invalid_expression1 = "+45"
invalid_expression2 = "17+4*"
invalid_expression3 = "(34+1"
invalid_expression4 = "45-3)"


print(is_valid_math_expression(valid_expression1))  # True
print(is_valid_math_expression(valid_expression2))  # True
print(is_valid_math_expression(valid_expression3))  # True
print(is_valid_math_expression(valid_expression4))  # True
print(is_valid_math_expression(invalid_expression1))  # False
print(is_valid_math_expression(invalid_expression2))  # False
print(is_valid_math_expression(invalid_expression3))  # False
print(is_valid_math_expression(invalid_expression4))  # False

