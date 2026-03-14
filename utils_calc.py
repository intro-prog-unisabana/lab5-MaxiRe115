def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2
def exponent(base, exp):
    return base ** exp
def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    else:
        return num1 % num2
import math 

def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        div= num1 / num2
        return math.floor(div)
def absolute(num):
    return abs(num)