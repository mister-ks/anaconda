
# coding: utf-8

# In[1]:

import csv


def prime_factorization(x, y):
    num = []
    while x >= y:
        if x % y == 0:
            x = x/y
            num.append(str(y))
        else:
            y += 1
    return num

with open('input.txt', 'r', encoding="utf-8_sig") as r:
    for line in r:
        with open('output.csv', 'a', encoding="utf-8_sig") as a:
            num = int(line)
            result = prime_factorization(num, 2)
            result.insert(0, str(num))
            writer = csv.writer(a, lineterminator='\n')
            writer.writerow(result)
