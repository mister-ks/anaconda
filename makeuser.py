
# coding: utf-8
class makedata:
    def __init__(self):
        print("Success a Instance!")

    def users(self):
        
# In[75]:

import random

alpha_list = []
res = []


def main():
    for i in range(48,48+10):
        alpha_list.append(chr(i))
    for i in range(97,97+26):
        alpha_list.append(chr(i))
    for i in range(65,65+26):
        alpha_list.append(chr(i))
        
    count = 0
    for count in range(100):
        numbers = range(61)
        alphas = [(n) for n in numbers]
    
        res = random.sample(alphas,6)
    
        print(alpha_list[res[0]]+alpha_list[res[1]]+alpha_list[res[2]]+alpha_list[res[3]]+alpha_list[res[4]]+alpha_list[res[5]])
    
        print(char)
        count = count + 1
main()


# In[73]:

alpha_list =[]

for i in range(97,97+26):
    alpha_list.append(chr(i))
    
print(alpha_list)


# In[43]:

import random

count = 0



# In[46]:

import random

r = range(10)

print(r)


# In[ ]:



