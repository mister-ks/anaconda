
# coding: utf-8

# In[10]:


def approximate(x, y, sum=0):
    for t in range(y, x+1):
        if x % t == 0:
            sum = sum + t
        if x % t != 0:
            pass
    print(sum)

approximate(26, 1)


# In[ ]:
