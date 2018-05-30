import numpy as np
import pandas as pd 

class linear_regression(object):

    def __init__(self):
        pass
    #对模型进行训练
    def fit(self,x,y):
        
        xx = x.as_matrix()
        yy = y.as_matrix()
        self.w = np.dot(np.dot(np.linalg.pinv(np.dot(xx.T,xx)),xx.T),yy)

    #返回洗漱
    def coef_(self):
        return self.w[:-1]

    #返回截距
    def intercept_(self):
        return self.w[-1,:]
    #对数据进行预测
    def predict(self,test_x):
        test_x = test_x.values
        self.predict_y = np.dot(test_x,self.w)
        return self.predict_y

    #对预测进行评估
    def mape(self,y_true):
        n = len(y_true)
        mape = sum((np.abs(y_true-self.predict_y))/y_true)/n *100
        return mape

#对数据进行划分，可以数用sklearn里的数据划分
def train_test_split(x,y,train_size = 0.7):
    n = int(len(y)*train_size)
    train_x = x[:n]
    train_y = y[:n]
    test_x = x[n:]
    test_y = y[n:]
    return train_x,test_x,train_y,test_y

def main():
    #获取数据
    file = 'C:\\Users\\Administrator\\Desktop\\challenge-1-beijing.csv'
    df = pd.read_csv(file)
    df['intercept'] = 1
    feature = df.drop(['小区名字','房型','每平米价格'],axis= 1)
    target = df['每平米价格']

    train_x,test_x,train_y,test_y = train_test_split(feature,target)

    model = linear_regression()
    model.fit(train_x,train_y)
    print(model.coef_()[:4])
    print(model.intercept_)

    model.predict(test_x)

    print(model.mape(test_y))

if __name__ =='__main__':
    main() 
