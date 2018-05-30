
# coding: utf-8

# In[1]:


from sklearn import datasets
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = datasets.load_breast_cancer()


# In[2]:


x = df.data
y = df.target


# In[3]:


f1 = plt.figure()
plt.scatter(x[y == 0,0],x[y ==0,1],color = 'r',label = df.target_names[0])
plt.scatter(x[y == 1,0],x[y ==1,1],color = 'g',label = df.target_names[1])
plt.xlabel(df.feature_names[0])
plt.ylabel(df.feature_names[1])
plt.legend()
plt.show()


# In[6]:


from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC


# In[13]:


train_x,test_x,train_y,test_y  = train_test_split(x,y)


# In[17]:


clf = SVC(kernel='linear')
clf.fit(train_x,train_y)
print(clf.score(test_x,test_y))


# In[20]:


clf = SVC(kernel='rbf')
clf.fit(train_x,train_y)
print(clf.score(test_x,test_y))


# In[41]:


from sklearn.neural_network import MLPClassifier
clf = MLPClassifier()
clf.fit(train_x,train_y)
print(clf.score(test_x,test_y))


# In[45]:


from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(train_x,train_y)
print(clf.score(test_x,test_y))

