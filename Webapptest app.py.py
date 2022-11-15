#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pywebio
from pywebio.input import *
from pywebio.output import *

input("What's your name?")
select("Select food", ['Orange','Apple'])
checkbox("Are you okay?",  options=["I'm Okay."])
radio("What do you like to do?", options=['Eat','Sleep','Study'])


# In[ ]:




