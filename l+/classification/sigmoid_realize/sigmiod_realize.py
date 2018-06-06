from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#define logistic regression
class logistic_regression(object):
    
    #initlization learning rate and number of iterations
    def __init__(self,lr = 0.3,num_iter = 10000):
        self.lr = lr
        self.num_iter = num_iter

    #fit feature target
    def fit(self,feature,target):
        self.all_loss = []
        ones = np.ones((len(target),1))
        feature = np.concatenate((ones,feature),axis = 1)
        self.w = np.zeros((feature.shape[1]))
        for num in range(self.num_iter):
            h = self.sigmoid(np.dot(feature,self.w))
            self.all_loss.append(self.loss(target,h))
            self.w -=self.lr * self.gardient(feature,target,h)
    
    #predict
    def predict(self,test_x):
        ones = np.ones((test_x.shape[0],1))
        test_x = np.concatenate((ones,test_x),axis = 1)
        self.pred_y = np.where(np.dot(test_x,self.w)>=0.5,1,0)
        return self.pred_y
    #obain the predict rate
    def socres(self,test_y):
        n = len(test_x)
        accr = np.sum(test_y == self.pred_y)
        return accr/n

    #obain coef
    def coef_(self):
        return self.w[1:]
    
    #obain intercept
    def intercept_(self):
        return self.w[0]
    
    
    def all_loss_func(self):
        return self.all_loss

    def sigmoid(self,z):
        return 1/(1+np.exp(-z))

    def loss(self,y,h):
        return (-y*np.log(h)-(1-y)*np.log(1-h)).mean()

    def gardient(self,x,y,h):
        return np.dot(x.T,h-y)/x.shape[0]

    
df = pd.read_csv('course-8-data.csv')

feature = df.iloc[:,:-1]
target = df.iloc[:,-1]

train_x,test_x,train_y,test_y = train_test_split(feature,target
                                                ,test_size = 0.3,random_state = 4)
model = logistic_regression(lr = 0.3,num_iter = 100)
model.fit(train_x,train_y)
model.predict(test_x)
print(model.socres(test_y))



        
