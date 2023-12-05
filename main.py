import re

def is_valid_math_expression(expr):
    # Шаблон поиска синтаксически корректных математических выражений
    pattern = r'^[\d\+\-\*/\(\)\s\w]+$'
    # Проверяем, соответствует ли строка шаблону
    if not re.match(pattern, expr):
        return False
    # Проверяем, что скобки расставлены правильно
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True

print(is_valid_math_expression('17*4+(x-54/(2+4))=y')) # True
print(is_valid_math_expression('2+2')) # True
print(is_valid_math_expression('18-41*с')) # True
print(is_valid_math_expression('+45')) # False
print(is_valid_math_expression('17+4*')) # False
print(is_valid_math_expression('(34+1, 45-3)')) # False
print(is_valid_math_expression('(4+5))')) # False