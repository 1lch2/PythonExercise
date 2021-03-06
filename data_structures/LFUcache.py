class Node:
    """Dual linked list node object.
    """
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.times = 0
        self.prev = None
        self.next = None
    
    def insert(self, position: "Node"):
        """Insert node object before the given position.
        """
        self.next = position
        self.prev = position.prev
        position.prev.next = self
        position.prev = self


class LFUCache:
    """LFU cache object.

    The cache with less using times are closer to head.

    If there are caches with same using times, the older one is closer to head.
    """
    def __init__(self, capacity: int):
        """Nodes are placed in ascending order of 'times' property.
        """
        self.cap = capacity
        self.cache = {} # {key: pointer}
        self.head = Node("#", "#")
        self.tail = Node("#", "#")
        
        self.head.next = self.tail
        self.tail.prev = self.head

        # Set the using times for head and tail node in order to judge and sort.
        self.head.times = -1
        self.tail.times = float("inf")


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key].times += 1

            temp = self.remove_node(self.cache[key])
            self.adjust(temp)

            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        """Update the LFU cache.
        """
        if self.cap == 0:
            return
            
        if key in self.cache:
            self.cache[key].times += 1 # Add using times
            self.cache[key].val = value # Update value
            temp = self.remove_node(self.cache[key])
            self.adjust(temp) # Adjust the location of the cache
        else:
            if len(self.cache) >=  self.cap:
                temp = self.remove_node(self.head.next) # Remove node from linked list
                self.cache.pop(temp.key) # Remove key-value pair from cache
                
            # Create new node and insert.
            temp = Node(key, value)
            self.cache[key] = temp

            self.adjust(temp)

    
    def remove_node(self, node: Node) -> Node:
        """Remove the node from linked list and return the pointer of the node.
        """
        # Remove from dual linked list
        node.prev.next = node.next
        node.next.prev = node.prev

        return node
    
    def adjust(self, node: Node):
        """Adjust the position of given node to suit the ascending order of times.
        
        With the while operation, the complexity is O(n)
        """
        #TODO: improve the time complexity to O(1)

        temp = self.tail

        # Find insert position
        while node.times < temp.prev.times and temp != self.head.next:
            temp = temp.prev
        # Check using times and insert the node
        if temp.prev.times <= node.times and node.times < temp.times:
            node.insert(temp)
