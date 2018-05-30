import numpy as np
import pandas as pd 

class polynomial_regression(object):

    def __init__(self,polynomial_n = 2):
        self.polynomial_n = polynomial_n        #本次需要的多项式的次数
    #对模型进行训练
    def fit(self,x,y):
        x_temp = self.feature_polynomil(x)
        x_temp.loc[:,'intercept'] = 1
        xx = x_temp.as_matrix()
        yy = y.as_matrix()
        self.w = np.dot(np.dot(np.linalg.pinv(np.dot(xx.T,xx)),xx.T),yy)

    #对数据集进行n次转化
    def feature_polynomil(self,x):
        polynomial_x = x
        for i in range(self.polynomial_n-1):
            for column in polynomial_x.columns:
                polynomial_x.loc[:,column + "_" + str(i)] = polynomial_x[column] ** (i+2)
        return polynomial_x        

    #返回系数
    def coef_(self):
        return self.w[:-1]

    #返回截距
    def intercept_(self):
        return self.w[-1,:]
    #对数据进行预测
    def predict(self,test_x):
        x_temp = self.feature_polynomil(test_x)
        x_temp.loc[:,'intercept'] = 1
        xx = x_temp.as_matrix()
        self.predict_y = np.dot(xx,self.w)
        return self.predict_y

    #对预测进行评估
    def mse(self,y_true):
        n = len(y_true)
        mse = sum((np.square(y_true-self.predict_y))/y_true)/n *100
        return mse

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
    for i in range(2,10):
        file = 'C:\\Users\\Administrator\\Desktop\\challenge-2-bitcoin.csv'
        df = pd.read_csv(file)
        feature = df[['btc_total_bitcoins','btc_transaction_fees']]
        target = df['btc_market_price']

        train_x,test_x,train_y,test_y = train_test_split(feature,target)
        
        model = polynomial_regression(i)
        model.fit(train_x,train_y)
        print("ceof:",model.coef_())
        print("intercept",model.intercept_)

        model.predict(test_x)

        print("mse:",model.mse(test_y))
        print('_________________________________')

if __name__ == "__main__":
    main() 