class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        child = Node(name)
        self.children.append(child)
        return child

    def bfs(self, array):
        queue = [self]
        
        while len(queue) > 0:
            node = queue.pop(0)
            array.append(node.name)
            for child in node.children:
                queue.append(child)
            
        return array


    def __repr__(self):
        return self.name


if __name__ == '__main__':
    a = Node("A")
    b = a.add_child("B")
    c = a.add_child("C")
    d = a.add_child("D")
    e = b.add_child("E")
    f = b.add_child("F")
    g = d.add_child("G")
    h = d.add_child("H")
    i = f.add_child("I")
    j = f.add_child("F")
    k = g.add_child("K")
    a.bfs([])

