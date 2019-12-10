#!/usr/bin/python3
for ones in range(0, 10):
    for tens in range(0, 10):
        if ones < tens:
            if ones < 8:
                print('{}{}'.format(ones, tens), end=', ')
            else:
                print('{}{}'.format(ones, tens))
