#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

length = len(argv)
if length == 1:
    print('{} arguments.'.format(length - 1))
elif length == 2:
    print('{} argument: '.format(length - 1))
    print('{}: {}'.format(1, argv[1]))
else:
    for i in range(length):
        if i == 0:
            print('{} arguments:'.format(length - 1))
        else:
            print('{}: {}'.format(i, argv[i]))
