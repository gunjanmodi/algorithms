class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

    def __repr__(self):
        return str(self.name)


if __name__ == '__main__':
    a, b, c, d, e, f, g, h, i, j, k = Node("A"), Node("B"), Node("C"), Node("D"), Node("E"), Node("F"), Node("G"), Node("H"), Node("I"), Node("J"), Node("K")
    a.add_child(b)
    a.add_child(c)
    a.add_child(d)

    b.add_child(e)
    b.add_child(f)

    f.add_child(i)
    f.add_child(j)

    d.add_child(g)
    d.add_child(h)

    g.add_child(k)

    array = []
    print(a.depth_first_search(array))

