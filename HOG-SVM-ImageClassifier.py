#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import cv2
from skimage.feature import hog
from sklearn.svm import SVC


# # 
# # Read Training Data & Extract Features

# In[2]:


trainPath = "D:\\Collge\\6th Term\\Pattern Recognition\\Assignments\\assignment 3\\Assignment dataset\\train"


# In[3]:


Categories = ['accordian', 'dollar_bill', 'motorbike', 'Soccer_Ball']


# In[4]:


xtrain = []
ytrain = []


# In[ ]:


i = 0
for category in Categories:
    categoryPath = os.path.join(trainPath,category)
    #print(categoryPath)
    for imgName in os.listdir(categoryPath):
        # Get the image
        imagePath = os.path.join(categoryPath,imgName)
        img = cv2.imread(imagePath)
        # Resize image
        img = cv2.resize(img, (128,64))
        # Extract image features
        fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8,8), cells_per_block=(2,2), visualize=True, multichannel=True)
        xtrain.append(fd)
        ytrain.append(i)
    i += 1


# In[6]:


xtrain = np.array(xtrain)
ytrain = np.array(ytrain)


# In[7]:


# Convert xtrain and ytrain arrays to pandas dataframe
df = pd.DataFrame(data=xtrain, columns=[f"hog_feature_{i}" for i in range(len(xtrain[0]))])
df['label'] = ytrain


# In[8]:


df.head()


# In[9]:


df.shape


# In[10]:


xtrain = df.drop(['label'], axis='columns')
ytrain = df.label


# # 
# # Models & Training

# In[11]:


model1 = SVC()
model1.fit(xtrain, ytrain)


# In[12]:


model2 = SVC(C = 1)
model2.fit(xtrain, ytrain)


# In[13]:


C = 1
model3 = SVC(kernel='linear',C=C)
model3.fit(xtrain, ytrain)


# In[14]:


kernelModel = SVC(kernel='linear')
kernelModel.fit(xtrain,ytrain)


# # 
# # Read Testing Data & Extract Features

# In[15]:


testPath = "D:\\Collge\\6th Term\\Pattern Recognition\\Assignments\\assignment 3\\Assignment dataset\\test"


# In[16]:


xtest = []
ytest = []


# In[ ]:


i = 0
for category in Categories:
    categoryPath = os.path.join(testPath,category)
    #print(categoryPath)
    for imgName in os.listdir(categoryPath):
        # Get the image
        imagePath = os.path.join(categoryPath,imgName)
        img = cv2.imread(imagePath)
        # Resize image
        img = cv2.resize(img, (128,64))
        # Extract image features
        fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8,8), cells_per_block=(2,2), visualize=True, multichannel=True)
        xtest.append(fd)
        ytest.append(i)
    i += 1


# In[18]:


# Convert xtest and ytest arrays to pandas dataframe
df2 = pd.DataFrame(data=xtest, columns=[f"hog_feature_{i}" for i in range(len(xtest[0]))])
df2['label'] = ytest


# In[19]:


df2


# In[20]:


xtest = df2.drop(['label'], axis='columns')
ytest = df2.label


# # 
# # Testing

# In[21]:


model1.score(xtest,ytest)


# In[22]:


model2.score(xtest,ytest)


# In[23]:


model3.score(xtest,ytest)


# In[24]:


kernelModel.score(xtest,ytest)

