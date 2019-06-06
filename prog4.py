#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fun(num):
    sum=0
    while num!=0:
        digit=num%10
        sum+=digit
        num=num//10
    print("sum is:",sum)

n=int(input("Enter number"))
fun(n)


# In[ ]:




