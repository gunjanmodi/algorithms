class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            node_temp = node
            node = node.next
            if node_temp.value == value:
                self.remove(node_temp)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.next.prev = node.prev
        if node.next is not None:
            node.prev.next = node.next
        node.next = None
        node.prev = None


    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            else:
                node = node.next
        return False
