# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

# get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
# put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。
# 当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。
# 在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
# 「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。


# 进阶：
# 你是否可以在 O(1) 时间复杂度内执行两项操作？


# 示例：
# LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回 1
# cache.put(3, 3);    // 去除 key 2
# cache.get(2);       // 返回 -1 (未找到key 2)
# cache.get(3);       // 返回 3
# cache.put(4, 4);    // 去除 key 1
# cache.get(1);       // 返回 -1 (未找到 key 1)
# cache.get(3);       // 返回 3
# cache.get(4);       // 返回 4

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
        """
        temp = self.tail

        # Find insert position
        while node.times < temp.prev.times and temp != self.head.next:
            temp = temp.prev
        # Check using times and insert the node
        if temp.prev.times <= node.times and node.times < temp.times:
            node.insert(temp)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    cache = LFUCache(0)
    res = []


    cache.put(0, 0)
    # cache.put(2, 2)

    # res.append(cache.get(1))
    
    # cache.put(3, 3)
    
    # res.append(cache.get(2))
    # res.append(cache.get(3))
    
    # cache.put(4, 4)
    
    # res.append(cache.get(1))
    # res.append(cache.get(3))
    res.append(cache.get(0))

    print(res)