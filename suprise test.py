#!/usr/bin/env python
# coding: utf-8

# In[24]:


items = [[12354, "Computer programming", 5, 449], [12355, "Programming for beginners", 8, 649], [12356, "Computer Basics", 3, 179]]

tota = lambda l: (l[1], l[2]*l[3])

print(list(map(tota,items)))


# In[22]:


units = int(input("Enter the number of units"))

if units in range(0,101):
    price = units * 1.00
elif units in range(101,201):
    price = units * 1.50
elif units in range(201,501):
    price = units * 3.00
elif units > 500:
    price = units * 5.00

print(price + (price*1.5/100))

