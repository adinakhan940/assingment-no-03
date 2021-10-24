#!/usr/bin/env python
# coding: utf-8

# # Assignmnet No : 03

# In[6]:


### question no:01 ###

print ("Twinkle,Twinkle,little star,
                 "How I Wonder That You Are!
                         "Up Above The world So High,
                         "Like A Diamond in The SKy.
       "Twinkle,Twinkle,little star,
                "How I Wonder That You Are")


# In[7]:


### Question no :02 ###

import sys
print ("Python Version")
print(sys.version)
print("Version info.")
print(sys.version_info)


# In[8]:


### Question no: 03 ###

import datetime
now = datetime.datetime.now()
print("current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S"))


# In[9]:


### QUestion no:04 ###

import math
radius = float(input("enter the radius of the circle :"))
area = math.pi * radius * radius 
print("area of the circle is : {0} ".format(area))


# In[10]:


### question no:05 ###

a = input("enter your first name")
b = input("enter your second name")
print(b + " " + a)


# In[11]:



### question no:06 ###

a = input("entyer your first name")
b = input("enter your second name")
c= a+b
print(c)


# In[12]:


### question no : 07 ###

eng = int(input("enter your eng marks"))
isl = int(input("enter your isl marks"))
math = int(input("enter your math marks"))
science = int(input("enter your science marks"))
urdu = int(input("enter your urdu marks"))

obtained_marks = eng + isl + math + science + urdu
print (obtained_marks)
total_marks = 500

percentage = obtained_marks / total_marks * 100

print(percentage)
percentage = 84.33333333333334

if percentage < 90 and percentage > 80 :
    print("grade A+")
elif percentage < 80 and  percentage > 70 :
    print("grade A")
elif percentage < 70 and percentage > 60 :
    print("grade B")
elif percentage < 60 and percentage  > 50 :
    print("grade C")
elif percentage < 50 and percentage  > 40 :
    print("grade D")
elif percentage < 40 and percentage  > 30 :
    print("grade E")
elif percentage < 30 and percentage  > 20 :
    print("grade F")
else:
    print ("FAil")
print ("Your_Total_marks_obtained is" , obtained_marks , "out of 300")
print ("your_percentage_is" , percentage )
print ("your_grade_is_A+")


# In[13]:


### question no:08 ###

n = int(input("Enter n : "))
if (n % 2 ==0):
    print(n,"is even number")
else:
    print(n,"is odd number")


# In[16]:


###question no:09 ###

list = [1,2,3,4,5,6]
count=0
for i in list:
    count = count + 1
print(count)
print(len(list))
    


# In[17]:


print(len(list))


# In[18]:


###question no:10 ###

list = [1,2,3,4,5,6]
b = sum(list)
print(b)


# In[28]:


### quetion no:11 ###

list  =[1,2,3,4,5,6]
largest = max(list)
print(f"largest is : {largest}")


# In[32]:


### question no :12 ###

list = [1,1,2,3,5,8,13,21,34,55,89]
print("the list in " +str(list))
new_list = []
for i in list:
    if i<5:
        new_list = new_list + [i]
print("new list :",new_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




