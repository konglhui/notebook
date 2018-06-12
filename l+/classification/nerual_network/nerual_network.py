import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def initialize_parameters_deep(layer_dims):         # 初始化参数
    # 输入：[输入层的shape[1]，各隐藏层的单元数，输出层的shape[0]]
    # 输出：各层的参数
    np.random.seed(1)
    parameters = {}
    L = len(layer_dims)

    for l in range(1, L):
        parameters['w' + str(l)] = np.random.randn(layer_dims[l],
                                                   layer_dims[l - 1]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))

    return parameters


def model_forward(X, parameters, activations):      # 前向传播
    # 输入：数据，参数,各层的激活函数列表
    # 输出：求得的y值和包含各层数据的存储器
    caches = []  # 存储器
    A = X

    # 开始各层循环计算得出求出Al,caches
    for i, activation in enumerate(activations):
        A_prev = A
        w = parameters['w' + str(i + 1)]
        b = parameters['b' + str(i + 1)]
        z = np.dot(w, A) + b
        if activation == "sigmoid":
            A = sigmoid(z)
        elif activation == "relu":
            A = relu(z)
        caches.append([A_prev, w, b, z])
    Al = A

    return Al, caches   # caches 包含每一层的 A_prev, W, b, Z


def compute_cost(AL, Y):  # 计算损失函数
    # 输入：y的计算输出值和真实值
    m = AL.shape[1]
    cost = (1. / m) * (-np.dot(Y, np.log(AL).T) -
                       np.dot(1 - Y, np.log(1 - AL).T))
    cost = np.squeeze(cost)
    return cost


def model_backward(AL, Y, caches, activations):     # 反向传播
    # 输入：y的预测值，y的真实值，各层数据
    # 输出：各层参数的倒数
    grads = {}
    L = len(caches)
    Y = Y.values.reshape(AL.shape)
    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    # 开始循环计算各层导数
    for l in reversed(range(L)):
        dA = dAL
        activation = activations[l]
        A_prev, w, _, z = caches[l]
        if activation == "relu":
            dz = relu_backward(dA, z)
        elif activation == "sigmoid":
            dz = sigmoid_backward(dA, z)
        m = A_prev.shape[1]
        dw = 1. / m * np.dot(dz, A_prev.T)
        db = 1. / m * np.sum(dz, axis=1, keepdims=True)
        dAL = np.dot(w.T, dz)

        grads["dw" + str(l + 1)] = dw
        grads["db" + str(l + 1)] = db

    return grads


def sigmoid(Z):                                 # 激活函数：sigmoid
    return 1 / (1 + np.exp(-Z))


def relu(Z):                                    # 激活函数：ReLU
    return np.maximum(0, Z)


def relu_backward(dA, z):                       # 对relu激活函数计算后向传播
    dZ = np.array(dA, copy=True)
    dZ = dA * np.where(z <= 0,0,1)
    return dZ


def sigmoid_backward(dA, z):                    # 对sigmoid激活函数计算后向传播
    s = 1 / (1 + np.exp(-z))
    dZ = dA * s * (1 - s)
    return dZ


def update_parameters(parameters, grads, learning_rate):  # 更新参数
    L = len(parameters) // 2
    for l in range(L):
        parameters["w" + str(l + 1)] = parameters["w" + str(l + 1)] - \
            learning_rate * grads["dw" + str(l + 1)]
        parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - \
            learning_rate * grads["db" + str(l + 1)]
    return parameters


def predict(X, y, parameters, activations):  # 预测新样本
    m = X.shape[1]
    p = np.zeros((1, m))

    # Forward propagation
    probas, _ = model_forward(X, parameters, activations)
    # convert probas to 0/1 predictions
    for i in range(0, probas.shape[1]):
        if probas[0, i] > 0.5:
            p[0, i] = 1
        else:
            p[0, i] = 0
            
    print("Accuracy: " + str(np.sum((p.reshape(m,) == y ))/ m))
    return  p.reshape(m,) , y


def main():
    # init parameters
    df = pd.read_csv(
        '/home/klh/file/github/notebook/l+/classification/sigmoid_realize/course-8-data.csv')
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    train_x, test_x, train_y, test_y = train_test_split(x, y,test_size = 0.3,random_state = 3)
    learning_rate = 1
    max_iter = 100
    layer_dims = [x.shape[1], 10, 5, 1]
    activations = ['relu', 'relu', 'sigmoid']
    init_parameter = initialize_parameters_deep(layer_dims)
    costs = []
    # iter cal y_pred
    for i in range(max_iter):
        parameter = init_parameter
        Al, caches = model_forward(train_x.T, parameter, activations)
        costs.append(compute_cost(Al,train_y.T))
        grads = model_backward(Al, train_y, caches, activations)
        init_parameter = update_parameters(parameter, grads, learning_rate)
    a = predict(test_x.T, test_y.values, init_parameter, activations)
    print(a)
    plt.plot([i for i in range(len(costs))],costs)
    plt.show()

if __name__ == '__main__':
    main()
