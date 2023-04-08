class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkedListNode(None, None)
        self.tail = DoublyLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        else:
            return None
            
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove_node(self.tail.prev)
            node = DoublyLinkedListNode(key, value)
            self.cache[key] = node
            self._add_to_front(node)

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# LRU Cache with cache eviction based on linear regression model
# from sklearn.linear_model import LinearRegression

# class LRUCacheWithML:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.head = DoublyLinkedListNode(None, None)
#         self.tail = DoublyLinkedListNode(None, None)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.regression_model = LinearRegression()

#     def get(self, key):
#         if key in self.cache:
#             node = self.cache[key]
#             self._move_to_front(node)
#             return node.value
#         else:
#             return None

#     def put(self, key, value):
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = value
#             self._move_to_front(node)
#         else:
#             if len(self.cache) == self.capacity:
#                 # Use the linear regression model to estimate the access frequency
#                 access_frequencies = [node.access_frequency for node in self.cache.values()]
#                 predicted_frequencies = self.regression_model.predict([[i] for i in access_frequencies])
#                 # Find the key of the least frequent node
#                 least_frequent_node_key = min(self.cache, key=lambda k: self.cache[k].access_frequency - predicted_frequencies[self.cache[k].access_frequency])
#                 del self.cache[least_frequent_node_key]
#                 self._remove_node(self.tail.prev)
#             node = DoublyLinkedListNode(key, value)
#             self.cache[key] = node
#             self._add_to_front(node)

#     def _move_to_front(self, node):
#         node.access_frequency += 1 # Increase the access frequency
#         self._remove_node(node)
#         self._add_to_front(node)

#     def _add_to_front(self, node):
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node

#     def _remove_node(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev

# class DoublyLinkedListNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#         self.access_frequency = 0 # Initialize access frequency to 0

