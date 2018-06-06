import numpy as np
import pandas as pd
import operator
from sklearn.model_selection import train_test_split
#knn classify
def knn_classify(train_x,train_y,test_x,n):
    pred_labels = []
    for pred_x in test_x:
        pred_distance = {}
        #要预测的点对每一个训练集进行计算距离
        for real_index,real_x in enumerate(train_x):
            distance = cal_distance(real_x,pred_x)
            pred_distance[real_index] = distance
        #找出最近的几个点.
        pred_distance = sort(pred_distance,False)
        label_counts = {}
        i = 0
        for label in pred_distance:
            i += 1
            if i < n + 1:
                label_counts[train_y[label[0]]] = label_counts.get(train_y[label[0]],0) + 1
            else:
                break
        label_counts = sort(label_counts)
        pred_labels.append(label_counts[0][0])
    return pred_labels,label_counts




#calucate the distance
def cal_distance(train_x,test_x):
    a = np.sum(np.sqrt(np.square(test_x-train_x)))
    return a 

def sort(x,judge = True):
    return sorted(x.items(),key = operator.itemgetter(1),reverse = judge)


df = pd.read_csv('/home/klinghui/file/github/notebook/l+/classification/knn_realize/course-9-syringa.csv')

feature = df.iloc[:,:-1]
target = df.iloc[:,-1]

train_x,test_x,train_y,test_y = train_test_split(feature.values,target.values,test_size = 0.3)
results,label_counts = knn_classify(train_x,train_y,test_x,5)
accu = np.sum(np.array(results) == test_y) / len(results)
print(accu)
print(results,test_y,label_counts)
