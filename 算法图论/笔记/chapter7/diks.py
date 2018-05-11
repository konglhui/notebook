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


