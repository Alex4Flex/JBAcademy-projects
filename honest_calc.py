import operator
from typing import List

messages: List[str] = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    ("Yes ... an interesting math operation. "
     "You've slept through all classes, haven't you?"),
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]


def is_number(var: str):
    try:
        float(var)
        return True
    except ValueError:
        return False


def do_operation(x, y, oper):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    return operations[oper](x, y)


def store_result_check():
    print(messages[4])
    answer = input()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        return store_result_check()


def continue_calc_check():
    print(messages[5])
    answer = input()
    if answer == 'y':
        return True
    elif answer != 'n':
        return continue_calc_check()
    return False


def is_one_digit(v):
    if abs(v) < 10 and v.is_integer():
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += messages[7]
    if (v1 == 0 or v2 == 0) and v3 in ['*', '+', '-']:
        msg += messages[8]
    if msg != "":
        msg = messages[9] + msg
        print(msg)


def save_memory_check(result):
    if not is_one_digit(result):
        return False
    msg_index = 10
    while msg_index <= 12:
        print(messages[msg_index])
        answer = input()
        if answer == 'y':
            msg_index += 1
        elif answer == 'n':
            return True
    return False


def honest_calc(memory=0):
    print(messages[0])
    x, oper, y = input().split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    if not is_number(x) or not is_number(y):
        print(messages[1])
        return honest_calc()

    x = float(x)
    y = float(y)

    if len(oper) != 1 or oper not in ['+', '-', '*', '/']:
        print(messages[2])
        return honest_calc()

    check(x, y, oper)

    if oper == '/' and y == 0:
        print(messages[3])
        return honest_calc()

    result = do_operation(x, y, oper)
    print(result)
    if store_result_check():
        if not save_memory_check(result):
            memory = result
    if continue_calc_check():
        return honest_calc(memory)


honest_calc()
