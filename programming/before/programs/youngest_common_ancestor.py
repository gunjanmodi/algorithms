import unittest

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None
        
def get_youngest_common_ancestor(topAncestor, descendantOne, descendantTwo):
    depth_one = get_top_descendant_depth(descendantOne, topAncestor)
    depth_two = get_top_descendant_depth(descendantTwo, topAncestor)

    if depth_one > depth_two:
        return backtrack_ancestor(descendantOne, descendantTwo, depth_one - depth_two)
    else:
        return backtrack_ancestor(descendantTwo, descendantOne, depth_two - depth_one)

def backtrack_ancestor(lower_descendant, higher_descendant, diff):
    while diff > 0:
        diff -= 1
        lower_descendant = lower_descendant.ancestor

    while higher_descendant != lower_descendant:
        higher_descendant = higher_descendant.ancestor
        lower_descendant = lower_descendant.ancestor
    return lower_descendant

def get_top_descendant_depth(descendant, topAncestor):
    depth = 0
    while topAncestor != descendant:
        depth += 1
        descendant = descendant.ancestor
    return depth


class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = get_youngest_common_ancestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])


if __name__ == '__main__':
    unittest.main()
