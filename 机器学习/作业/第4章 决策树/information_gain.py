import pandas as pd 
import math
#生成节点
#attr 保存当前节点的属性
#label 保存当前结点的标签
#attr_down 保存当前结点的子孙节点，
class Node(object):
    def __init__(self,attr_init = None,label_init = None, attr_down_init = {}):
        self.attr = attr_init
        self.label = label_init
        self.attr_down = attr_down_init

# 生成树
# dataset 就是一个pandas的dataframe的数据集
def tree_generate(dataset):
    new_node = Node(None,None,{})
    label_attr = dataset[dataset.columns[-1]]

    label_count = classify_label(label_attr)

    if label_count :  #当前结点是非空集合
        new_node.label = max(label_count,key = label_count.get)

        #当前结点所有标签只有一个属性
        if len(label_count) == 1:
            return new_node
        
        #从A中选出最优划分属性attr
        new_node.attr = attr_separation(dataset)

        #按照属性进行划分
        value_count = classify_label(dataset[new_node.attr])
        for value in value_count:
            dataset_v = dataset[dataset[new_node.attr].isin[value]]  
            dataset_v = dataset_v.drop(new_node.attr, 1)  
            new_node.attr_down[value] = tree_generate(dataset_v)
        
    return new_node





#将当前的标签进行分类，目的是检查当前的标签有几类。
def classify_label(label_attr):
    label_count = {}

    for item in label_attr[label_attr]:
        if item in label_count:
            label_count[item] +=1
        else:
            label_count[item] = 1
    return label_count


#dataset 数据集
#对使用信息熵和信息增益，选择信息增益最大的属性，并属性进行划分。
def attr_separation(dataset):
    info_gain = 0
    divide_name = ' '
    for attr_key in dataset.columns[1:-1]:
        temp_info_gain = information_gain(dataset,attr_key)
        if info_gain < temp_info_gain:
            info_gain = temp_info_gain
            divide_name = attr_key
    return divide_name






#计算信息增益
def information_gain(dataset,attr_key):
    #计算总的信息熵
    count = 0
    ent_label_count = classify_label(dataset[dataset.columns[-1]])
    for value in ent_label_count.values():
        count += value
        num = value
    ent = information_entropy(count,num)

    #计算信息增益
    single_ent_label = classify_label(dataset[attr_key])
    for item,count in single_ent_label.items():
        double_dataset = dataset[dataset.columns[-1]]
        data = double_dataset[attr_key==item]
        set_num = classify_label(data)
        for item in set_num.values():
            num = item
        ent -= information_entropy(count,num)
    return ent


#计算信息熵
#count:样例的总数
#num  :正例的个数
def information_entropy(count,num):
    return -(num/count*(math.log2(num/count)) + (count-num)/count * math.log2((count-num)/count))

def main():
    data = pd.read_csv('C:/Users/Administrator/Desktop/123.csv',encoding= 'ANSI')

    tree = tree_generate(data)
    if key in tree.attr_down: 
        root = root.attr_down[key]
        print(root)

main()

