
# coding: utf-8

# In[3]:

import csv

f = open('f:/Finance/クレジットカード/BILL1706.csv')

s = csv.reader(f, delimiter=' ', quotechar='|')
for row in s:
    print(','.join(row))

# In[8]:

from urllib import request

r = request.Request('http://www.yahoo.co.jp')

g = r.get_method()

print(g)


# In[ ]:
