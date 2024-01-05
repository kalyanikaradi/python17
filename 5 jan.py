#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip show pip


# In[2]:


pip install camelcase


# In[5]:


#camelcase trurns all starting word into capital
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


# In[12]:


#findall returns matches
import re

txt='the rain in spain'
x=re.findall("ai",txt)
print(x)


# In[13]:


import re
txt = 'the rain in spain'
x=re.findall('portugal',txt)
print(x)


# In[14]:


#search will search and return matching obj
import re
txt = 'the rain in spain'
x=re.search('in',txt)
print(x)


# In[15]:


import re
txt = 'the rain in spain'
x=re.findall('portugal',txt)
print(x)


# In[16]:


#split at each white space
import re
txt = 'the rain in spain'
x=re.split('n',txt)
print(x)


# In[20]:


import re
txt = 'the rain in spain'
x=re.split('t',txt)
print(x)


# In[22]:


#sub Replace every white-space character with the number 


import re
txt = 'the rain in spain'
x=re.sub('t','9',txt)
print(x)


# In[26]:


import re
txt = 'the rain in spain'
x=re.sub('i','3',txt)
print(x)


# In[ ]:




