#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os


# In[2]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# In[3]:


img = cv2.imread('test.jpg')


# In[4]:


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[5]:


faces = face_cascade.detectMultiScale(gray, 1.1, 4)


# In[6]:


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


# In[7]:


cv2.imshow('img', img)
cv2.waitKey()


# In[ ]:




