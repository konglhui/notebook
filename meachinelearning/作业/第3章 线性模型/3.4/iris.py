
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.model_selection import cross_validate
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


# In[4]:


iris = datasets.load_iris()


# In[5]:


log = LogisticRegression()


# In[6]:


from sklearn.model_selection import cross_val_score
scores = cross_val_score(log,iris.data,iris.target,cv = 10)
print(sum(scores)/10)


# In[14]:


from sklearn.model_selection import LeaveOneOut
accurcay = 0
loo = LeaveOneOut()
for train, test in loo.split(iris.data):
    log.fit(iris.data[train],iris.target[train])
    y_p = log.predict(iris.data[test])
    if y_p == iris.target[test]:
        accurcay +=1
print(accurcay/np.shape(iris.target)[0])

