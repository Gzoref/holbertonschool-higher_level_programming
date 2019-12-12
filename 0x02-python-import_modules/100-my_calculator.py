#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        if operator == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif operator == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif operator == '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif operator == '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
