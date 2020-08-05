
# lfu design
# @param operators int整型二维数组 ops
# @param k int整型 the k
# @return int整型一维数组

# TODO: Not tested yet

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.times = 0
        self.prev = None
        self.next = None


class Solution:
    def LFU(self , operators: list , k: int):
        # write code here
        def __init__(self, k):
            self.cap = k
            self.map = {}
            
            self.head = Node("#", "#")
            self.tail = Node("#", "#")
            
            self.head.next = self.tail
            self.tail.prev = self.head
        
        def set(self, key, value):
            if key in self.map:
                self.map[key].times += 1
                temp = self.remove_node(self.map[key])
                self.move_to_end(temp)
            else:
                if len(self.map) < self.cap:
                    temp = Node(key, value)
                    self.map[key] = temp

                    temp.next = self.tail
                    temp.prev = self.tail.prev
                    self.tail.prev.next = temp
                    self.tail.prev = temp
                    
                else:
                    self.remove_node(self.head.next)
                    
                    temp = Node(key, value)
                    self.map[key] = temp

                    temp.next = self.tail
                    temp.prev = self.tail.prev
                    self.tail.prev.next = temp
                    self.tail.prev = temp
            
            
        def get(self, key):
            if key in self.map:
                self.map[key].times += 1
                temp = self.remove_node(self.map[key])
                self.move_to_end(temp)
                return self.map[key].val
            else:
                return -1
            
            
        def move_to_end(self, node):
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            
        
        def remove_node(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            
            return node
            