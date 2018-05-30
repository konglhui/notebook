
# coding: utf-8

# In[23]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# In[36]:


dataset = np.loadtxt('C:/Users/Administrator/Desktop/melon.csv', delimiter=",")


# In[40]:


y = dataset[:,3]
X = dataset[:,1:3]


# In[44]:


f1 = plt.figure(1)
plt.title("which is good melon")
plt.xlabel('density')
plt.ylabel('suger_content')
plt.scatter(X[y == 0,0], X[y == 0,1], marker = 'o', color = 'k', s=100, label = 'bad')
plt.scatter(X[y == 1,0], X[y == 1,1], marker = 'o', color = 'g', s=100, label = 'good')
plt.legend(loc = 'upper right')
plt.show()



# In[46]:


from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# In[49]:


x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.5, random_state=0)


# In[50]:


log_model = LogisticRegression()
log_model.fit(x_train,y_train)


# In[51]:


y_pred = log_model.predict(x_test)
print(metrics.confusion_matrix(y_test,y_pred))
print(metrics.classification_report(y_test,y_pred))

