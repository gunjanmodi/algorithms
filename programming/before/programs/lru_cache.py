import unittest

class LRUCache:
    def __init__(self, max_size):
        self.cache = {}
        self.current_capacity = 0
        self.max_size = max_size or 1
        self.list_of_most_recent = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.current_capacity == self.max_size:
                self.evict_least_recent()
            else:
                self.current_capacity += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.cache[key].value = value
        self.update_most_recent(self.cache[key])
        
    def update_most_recent(self, node):
        self.list_of_most_recent.set_head(node)

    def evict_least_recent(self):
        key_to_remove = self.list_of_most_recent.tail.key
        self.list_of_most_recent.remove_tail()
        del self.cache[key_to_remove]

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        node_to_return = self.cache[key]
        self.update_most_recent(node_to_return)
        return node_to_return.value

    def getMostRecentKey(self):
        if self.list_of_most_recent.head is None:
            return None
        return self.list_of_most_recent.head.key

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None




class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def remove_bindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        lruCache = LRUCache(3)
        lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("a", 1)
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getMostRecentKey(), "c")
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getMostRecentKey(), "a")
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        lruCache.insertKeyValuePair("a", 5)
        self.assertEqual(lruCache.getValueFromKey("a"), 5)


if __name__ == '__main__':
    unittest.main()