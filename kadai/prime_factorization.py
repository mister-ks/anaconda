
# coding: utf-8


def prime_factorization(x, y):
    while x >= y:
        if x % y == 0:
            x = x/y
            print(y)
        else:
            y += 1

prime_factorization(180, 2)
