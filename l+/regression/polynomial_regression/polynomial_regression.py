import numpy as np
import pandas as pd 

class polynomial_regression(object):

    def __init__(self):
        pass
    #对模型进行训练
    def fit(self,x,y):
        xx = x.as_matrix()
        yy = y.as_matrix()
        self.w = np.dot(np.dot(np.linalg.pinv(np.dot(xx.T,xx)),xx.T),yy)

    #返回系数
    def coef_(self):
        return self.w[:-1]

    #返回截距
    def intercept_(self):
        return self.w[-1,:]
    #对数据进行预测
    def predict(self,test_x):
        xx = test_x.as_matrix()
        self.predict_y = np.dot(xx,self.w)
        return self.predict_y

    #对预测进行评估
    def mse(self,y_true):
        mse = sum(np.square(y_true-self.predict_y)/len(y_true))
        return mse

#对数据进行划分，可以数用sklearn里的数据划分
def train_test_split(x,y,train_size = 0.7):
    n = int(len(y)*train_size)
    train_x = x[:n]
    train_y = y[:n]
    test_x = x[n:]
    test_y = y[n:]
    return train_x,test_x,train_y,test_y


#对数据集进行n次转化 
def feature_polynomil(x,n = 2):
    for i in range(1,n):
        a = x.columns
        for column in  a:
            x[column + "-" + str(i)] = x.loc[:,column]**(i+1)
    return x       

def main():
    #获取数据
    file = 'E:\\klinghui\\notebook\\l+\\regression\\polynomial_regression\\challenge-2-bitcoin.csv'
    df = pd.read_csv(file)
    feature = df[['btc_total_bitcoins','btc_transaction_fees']]
    target = df['btc_market_price']
    n_feature = feature_polynomil(feature,n = 5)
    n_feature.dropna(inplace=True)
    train_x,test_x,train_y,test_y = train_test_split(n_feature,target)
    
    model = polynomial_regression()
    model.fit(train_x,train_y)
    model.predict(test_x)

    print("mse:",model.mse(test_y))
    print('_________________________________')

if __name__ == "__main__":
    main() 