#!/usr/bin/python3
for letter in range(25, -1, -1):
    alphabet = letter + ord('A')
    if letter % 2 == 1:
        alphabet += 32
    print('{:c}'.format(alphabet), end='')
