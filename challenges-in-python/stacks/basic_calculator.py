# Solving the "Basic Calculator" Challenge
# Challenge Description:
# Implement a basic calculator to evaluate a simple expression string. 
# The expression string may contain open '(' and closing parentheses ')', 
# the plus '+' or minus sign '-', non-negative integers, and empty spaces ' '. 
# The expression string contains only non-negative integers, '+', '-', '*', '/', parentheses, 
# and empty spaces. The integer division should truncate toward zero.

# Approach:
# Use two stacks: one for numbers and another for operators, 
# including parentheses. Parse through the string, applying the appropriate operations and respecting the precedence defined by parentheses.

def calculate(s: str) -> int:
    def apply_operator(a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a // b
        
    def precedence(op1, op2):
        if op2 == '(' or op2 == ')':
            return False
        if (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
            return False
        return True
    
    numbers = []
    operators = []
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        elif s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            numbers.append(num)
        elif s[i] == '(':
            operators.append(s[i])
            i += 1
        elif s[i] == ')':
            while operators and operators[-1] != '(':
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(apply_operator(a, b, operators.pop()))
            operators.pop()
            i += 1
        else:
            while operators and precedence(s[i], operators[-1]):
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(apply_operator(a, b, operators.pop()))
            operators.append(s[i])
            i += 1

    while operators:
        b = numbers.pop()
        a = numbers.pop()
        numbers.append(apply_operator(a, b, operators.pop())) 
    return numbers.pop()

# Testing the function
def test_calculate():
    assert calculate("3+2*2") == 7
    assert calculate("3/2") == 1
    assert calculate("3+5/2") == 5
    assert calculate("(3+5)/2") == 4
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23

test_calculate()

print(calculate("999/(9+9+9)"))
print(calculate("666/(6+6+6)"))
print(calculate("555/(5+5+5)"))
print(calculate("444/(4+4+4)"))