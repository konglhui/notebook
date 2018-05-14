# -*-coding:utf-8-*-  
# 用散列表实现图的关系
graph = {}  
graph["start"] = {}  
graph["start"]["a"] = 6  
graph["start"]["b"] = 2  
graph["a"] = {}  
graph["a"]["end"] = 1  
graph["b"] = {}  
graph["b"]["a"] = 3  
graph["b"]["end"] = 5  
graph["end"] = {}  

#定义路径数据类型，保存具体的路径和路径的总长度。
class Path(object):

    def __init__(self,path_init = [],length_init = 0):
        self.path = path_init
        self.length = length_init


def diks(graph):
    optimal_path = Path([],0)#保存最优路径

    nodes = graph["start"]
    all_path = {}#保存所有节点的距离，进行比较
    while nodes :
        temp_length = 999
        optimal_node = ' '
        for node,path_length in nodes.items():
            #保存所有节点的的路径和距离
            temp_node = Path([],0)
            for item in optimal_path.path:
                temp_node.path.append(item)
            temp_node.length += optimal_path.length
            temp_node.path.append(node)
            temp_node.length += path_length
            if node in all_path.keys():
                if all_path[node].length > optimal_path.length+path_length:
                    all_path[node] = temp_node
            else:
                all_path[node] = temp_node
            #选择最优距离
            if path_length < temp_length:
                optimal_node = node
                temp_length = path_length


        optimal_path.length += temp_length
        optimal_path.path.append(optimal_node)
        
        #判断是否有更优的节点
        if all_path[optimal_path.path[-1]].length < optimal_path.length:
            optimal_path.length =  all_path[optimal_path.path[-1]].length
            for item in all_path[optimal_path.path[-1]].path:
                optimal_path.path.append(item)
            

        nodes = graph[optimal_node]
    
    for item in optimal_path.path:
        print(item)

    print(optimal_path.length)

diks(graph)



