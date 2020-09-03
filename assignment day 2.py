#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A list is a container which can hold diffrent data types in it.
lst=["Swathi",15,8790,[9,8,5],"Priya"]


# In[2]:


lst


# In[3]:


lst[0]


# In[5]:


lst[3][1]


# In[6]:


lst.append("sumiya")


# In[7]:


lst


# In[9]:


lst.index(15)


# In[10]:


lst[-1]


# In[11]:


lst[-4]


# In[12]:


lst[4]


# In[13]:


lst[3][2]


# In[14]:


#It is complex,this is a key value pair data structure


# In[22]:


dit={"name ":"Swathipriya","age":"20","phone number":"123456789"}


# In[23]:


dit


# In[28]:


dit.items()


# In[29]:


dit.keys()


# In[34]:


dit


# In[35]:


dit["School"]="GEMS"


# In[36]:


dit


# In[37]:


type(dit)


# In[41]:


#sets are used for string unique values in the python


# In[42]:


st={"kumari","Google",1,1,2,4,8,5,2,9}


# In[43]:


st


# In[46]:


st2={"Google",2}


# 

# In[48]:


st2.issubset(st)


# In[49]:


#tuples are ordered immutable collection of objects


# In[50]:


tup=("Swathi","%","swathi@com")


# In[51]:


tup


# In[52]:


tup.count("%")


# In[53]:


tup.index("swathi@com")


# In[54]:


#String is  ordered sequence of characters


# In[55]:


name="Swathi"
name1="Soumya"


# In[57]:


name1


# In[58]:


name+" "+name1


# In[59]:


type(name)


# In[ ]:




