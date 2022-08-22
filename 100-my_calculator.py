#!/usr/bin/python3


if __name__ == "__main__" :
    from calculator_1 import add, sub, mul, div
    import sys

    args_sum = len(sys.argv) -1
    operators = ['+', '-', '*', '/']

    if args_sum != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv [2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = sys.argv [1]
    b = sys.argv [3]
    operator = sys.argv [2]
    if operator == operators [0]:
        print("{} {} {} = {}".format(a, operator, b, add(int(a), int(b))))
    elif operator == operators [1]:
        print("{} {} {} = {}".format(a, operator, b, sub(int(a), int(b))))
    elif operator == operators [2]:
        print("{} {} {} = {}".format(a, operator, b, mul(int(a), int(b))))
    elif operator == operators [3]:
        print("{} {} {} = {}".format(a, operator, b, div(int(a), int(b))))
