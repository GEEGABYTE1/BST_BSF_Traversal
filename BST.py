import random
from Queue import Queue

class BST:
    queue = Queue()
    def __init__(self, value, depth=1):
        self.value = value 
        self.depth = depth 
        self.right = None
        self.left = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left == None:
                self.left = BST(new_value, self.depth + 1)
                print("Node {value} has been added to the left of {parent} at depth {depth}".format(value=new_value, parent=self.value, depth=self.depth + 1))
            else:
                self.left.insert(new_value)

        else:
            if self.right == None:
                self.right = BST(new_value, self.depth + 1)
                print('Node {value} has been added to the right of {parent} at depth {depth}'.format(value=new_value, parent=self.value, depth=self.depth + 1))
            else:
                self.right.insert(new_value)


    def get_node_by_value(self, value):
        if value == self.value:
            return self.value 
        elif self.left and value < self.value:
            return self.left.get_node_by_value(value)
        elif self.right and value >= self.value:
            return self.right.get_node_by_value(value)
        else:
            return None 

    
    ### 

    def breadth_first_traversal(self, path):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            self.queue.enqueue(current_node.value)
            if not current_node.right and not current_node.left:
                pass
            elif not current_node.right:
                nodes.append(current_node.left)
            elif not current_node.left:
                nodes.append(current_node.right)
            else:
                nodes.append(current_node.right)
                nodes.append(current_node.left)
        
        while self.queue.head_node != None:
            print(self.queue.dequeue())

    ###



         

    def depth_first_traversal(self):
        if self.left:
            self.left.depth_first_traversal()
        print('Depth: {depth}, Value: {value}'.format(depth=self.depth, value=self.value))
        if self.right:
            self.right.depth_first_traversal()


test = BST(1)


test.insert(10)
test.insert(2)
test.insert(10)
test.insert(18)
print(test.depth_first_traversal())
print()
print(test.breadth_first_traversal(test))

