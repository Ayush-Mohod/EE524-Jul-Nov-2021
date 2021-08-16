#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
print("Hello world")


# In[2]:


#Q2
a=int(input("enter first no."))
b=int(input("enter second no."))
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a%b=",a%b)


# In[3]:


#Q3
num=int(input("Enter number to find factorial"))
fact=1
for i in range (1, num+1):
    fact=fact*i
print("factorial of a number is",fact)


# In[5]:


#Q4
a=int(input("Enter first no."))
b=int(input("Enter second no."))
for i in range(a,b+1):
    if i>1:
        for j in range (2,i):
            if(i%j)==0:
                break
            else:
                print(i)
               


# In[7]:


#Q5
def lcmcal(a,b):
    if a>b:
        max=a
    else:
        max=b
    while(True):
        if((max%a==0) and (max%b==0)):
            lcm=max
            break
        max+=1
    return lcm

x=int(input("enter first no."))
y=int(input("enter second no."))

print("LCM of two no. is",lcmcal(x,y))


# In[9]:


#Q6
def bubblesort(theseq):
    n=len(theseq)
    for i in range (n-1):
        flag=0
        for j in range (n-1):
            if theseq[j]<theseq[j+1]:
                tmp=theseq[j]
                theseq[j]=theseq[j+1]
                theseq[j+1]=tmp
                flag=1
        if flag==0:
            break
    return theseq
     

e1=[21,6,9,33,3,8,7,2,1,66,23,25,31,40]
result=bubblesort(e1)
print(result)


# In[11]:


#Q7
import numpy as np

array=np.array([21,6,9,33,3,8,7,2,1,66,23,25,31,40])
ascend_array=np.sort(array)
descend_array=ascend_array[::-1]
print(descend_array)


# In[12]:


#Q8
row_num=int(input("input no. of rows"))
col_num=int(input("input no. of columns"))
multi_list=[[0 for col in range(col_num)] for row in range(row_num)]
for row in range (row_num):
    for col in range(col_num):
        multi_list[row][col]=row*col
print(multi_list)


# In[ ]:




