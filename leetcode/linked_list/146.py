# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。

# 当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

# 进阶:
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？

# 示例:
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4

class DLNode:
    """Dual linked list node object.
    """
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """A LRU cache object that implements the LRU memory page swap algorithm

    Attributes:
        head: Dummy head of cache linked list, referring to the rarely accessed cache.
        tail: Dummy tail of cache linked list, referring to the latest accessed cache.
        cap: The capacity of the LRU cache.
        cache: A dict object with cached key-value pairs.
    """
    def __init__(self, capacity: int):
        """Initialize the LRUCache object with desired capacity

        Args:
            capacity: The desired capacity number of the LRU cache.
        """
        # Initialize dummy nodes
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        # Initialize cache.
        self.cap = capacity
        self.cache = {}

    def move_to_end(self, key):
        """Move the node that match the key to the end positon of the linked list.
        Args:
            key: Key of target node.
        """
        # Get the target node.
        node = self.cache[key]

        # Remove the node from dual-linked list
        node.prev.next = node.next
        node.next.prev = node.prev

        # Add the node before the dummy tail node.
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        """Get the node value of given key.
        """
        if key in self.cache:
            self.move_to_end(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """Add or update the given node.
        """
        # If key in cache
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_end(key)
        else:
            # Check the capacity
            if len(self.cache) == self.cap:
                # Remove the most rarely used node.
                self.cache.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            
            new_node = DLNode(key, value)
            # Insert the new node into linked list and cache table.
            self.cache[key] = new_node
            
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node
