#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except Exception as TE:
        print('Exception: {}'.format(TE), file=stderr)
        return False
    return True
