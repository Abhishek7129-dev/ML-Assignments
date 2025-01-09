#!/usr/bin/env python
# coding: utf-8

# Lambda Functions

# In[10]:


greet = lambda name : print(f"Good Morning {name}!")
greet("Abhishek")


# In[20]:


product = lambda a,b,c :a*b*c
product(20,30,40)


# In[22]:


even = lambda L: [x for x in L if x % 2 == 0]
my_list = [100, 3, 9, 38, 43, 56, 20]
print(even(my_list))


# In[ ]:




