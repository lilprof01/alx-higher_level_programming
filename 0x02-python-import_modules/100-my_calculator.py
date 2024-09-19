if __name__ == '__main__':
    import sys
    ac = sys.argv[1:]
    if len(ac) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(ac[0])
    b = int(ac[2])
    if ac[1] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif ac[1] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif ac[1] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif ac[1] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
