#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
        return result
    except Exception as err:
        print('Exception: {}'.format(err), file=stderr)
        return None
