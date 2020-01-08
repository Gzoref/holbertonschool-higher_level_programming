#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for items in range(x):
        try:
            print('{}'.format(my_list[items]), end='')
            index += 1
        except IndexError:
            break
    print()
    return index
