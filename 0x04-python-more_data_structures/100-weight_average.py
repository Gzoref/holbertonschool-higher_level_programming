#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    product = []
    for i in my_list:
        weight += i[1]
        product.append(i[0] * i[1])
    return sum(product) / weight
