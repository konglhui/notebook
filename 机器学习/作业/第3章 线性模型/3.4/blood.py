
# coding: utf-8

# In[1]:


import  numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict


# In[8]:


data = np.loadtxt(open('E:/klinghui/00/blood1.csv'),delimiter = ',')


# In[9]:


print(data)


# In[17]:


X = data[:,0:-1]
y = data[:,-1]
print(X,y)


# In[18]:


from sklearn import metrics
log = LogisticRegression()
y_pred = cross_val_predict(log,X,y,cv =10)
print (metrics.accuracy_score(y,y_pred))


# In[21]:


from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
accuracy = 0
for train,test in loo.split(X):
    log.fit(X[train],y[train])
    y_p = log.predict(X[test])
    if y_p == y[test]:
        accuracy += 1
print(accuracy / np.shape(X)[0])

