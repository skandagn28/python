#!/usr/bin/env python
# coding: utf-8

# In[11]:


lst=[1,2,3]
lst6=[str(item)+"s" for item in lst]
print(lst6)


# In[17]:


print([item**2 for item in lst])


# In[19]:


def ipsplitter(s):
    return s.split(".")
print(ipsplitter("192.168.1.1"));


# In[20]:



def fruitsplitter(s):
    return s.split("#")
print(fruitsplitter("apple#orange#grapes#banana"));


# In[21]:




def phonenumber(ph):
    return ph[:2]+"-"+ph[2:]
print(phonenumber("919789090840"))


# In[ ]:




def phonenumber(ph):
    return ph[2:]
print(phonenumber("919789090840"))


# In[ ]:



def phonenumber(ph):
    return ph.replace("-","")
print(phonenumber("91-9789090840"))


# In[23]:


employee=[(1,2,3),(4,5,6),(7,8,9)]
employee[0]=(3,5,8)
print(employee)


# In[32]:


employee = {"name": "john", "Age":20, "city":"dubai"}
print(employee['Age'])
print(employee.keys())
print(employee.values())
print(employee.get("name"))


# In[41]:


colors={"pink", "yellow", "green"}
colors.update(['orange','black'])
colors.remove('orange')
colors.add('blue')
print(colors)
print(len(colors))


# In[42]:


rep=[1,2,3,4,5,4,3,2]
uniq=set(rep)
print(uniq)


# In[46]:


tup=[(1,2),(4,5)]
dic=dict(tup)
print(dic)


# In[53]:


inp=str(input("Enter the name "))
if inp=="1":
    print("{} is one".format(inp))
elif inp=="2":
    print("{} is two".format(inp))
elif inp=="3":
    print("{} is three".format(inp))


# In[58]:


a=27
print("a") if a==10 else print("b") if a==20 else print("c")


# In[62]:


i=(10,20,30)
for j in i:
    print(j)
    if(j==20):
        break;


# In[ ]:


for i in range(1,11):
    print()
    for j in range(1,i):
        print(j, end="   ")
    


# In[1]:


for value in range(5):
     print(value)
else:
    print("unconditional man! are u fool! why are uy giving this *")


# In[5]:


i=1
j=10
num=int(input("Enter the number"))
while(i<=j):
    print("{}x{}={}".format(num,i,num*i))
    i+=1


# In[12]:


x=1
y=100
num=int(input("Enter the number"))
for i in range(x,y+1,5):
    print("{}^{}={}".format(num,i,num**i))


# In[6]:


for x in range(0,10):
    if x==5:
        print("Inside pass {}".format(x))
        pass
        print("After pass {}".format(x))
    print(x)
    


# In[96]:


l=[];
    
def rec(y):

    for x in y:
        if type(x) is list or type(x) is tuple or type(x) is set:
            rec(x)
        else:
            l.append(x)
    return l

lst=[10,['user1','user2',{"user4", 15}],10.25, ('test1', 'test2'), True, None]
print(rec(lst));


# In[62]:


size = 5
for i in range(0,size+1):
    print("")
    for k in range(0,i):
        print("*", end="")
    for j in range(0,size - i):
        print(" ", end=" ")
    for k in range(0,i):
        print("*", end="")
for i in range(0,size+1):
    print("")
    for k in range(0,size - i):
        print("*", end="")
    for j in range(0,i):
        print(" ", end=" ")
    for k in range(0,size - i):
        print("*", end="")


# In[68]:


size = 5
for i in range(0,size+1):
    print("")
    for k in range(0,size*2 - i*2):
        print(" ", end="")
    for j in range(0,i):
        print("*", end="   ")


# In[82]:


movies = ["The Holy Grail", "Life of brain", "Meaning of life"]
years = [1975,1979,1983]
output = []
for (movie, year) in zip(movies, years):
    output.append(movie)
    output.append(year)
print(output)                       


# In[92]:


import random
com = random.randint(1,10)
victory=0
for i in range(0,6):
    guess=int(input("Guess something "))
    if guess>com:
        print("Your guess is too high")
    elif guess<com:
        print("Your guess is too low")
    else:
        print("You guessed right!")
        victory=1
        break
if victory==0:
    print("Failed to guess! Better luck next time.")


# In[100]:


year=int(input("Enter year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap year")
else:
    print("Not a leap year")

