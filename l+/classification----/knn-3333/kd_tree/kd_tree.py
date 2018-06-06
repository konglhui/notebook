import operator

#create tree node
class Node(object):
    def __init__(self):
        self.data = []
        self.l_child = None
        self.r_child = None


#create kd tree
class kd_tree(Node):
    def create_tree(self,tree,point_list,depth = 0):
        
        #dataset isn't empty
        if not point_list:
            return None
        
        #Gets the median of the remaining number
        axis = depth%len(point_list[0])
        point_list.sort(key = operator.itemgetter(axis))
        median = len(point_list)//2 

        #create node and subtree
        tree.data = point_list[median]
        tree.l_child = Node()
        tree.r_child = Node()
        self.create_tree(tree.l_child,point_list[:median],depth + 1)
        self.create_tree(tree.r_child,point_list[median+1:],depth + 1)

    #visit a tree node
    def visit(self,tree):
        if tree is not None:
            print(str(tree.data) + "\t")

    def pre_order(self,tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.l_child)
            self.pre_order(tree.r_child)


def main():
    """Example usage"""
    point_list = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    t = Node()
    tree = kd_tree()
    tree.create_tree(t, point_list)
    tree.pre_order(t)

if __name__ == '__main__':
    main()
        
        
