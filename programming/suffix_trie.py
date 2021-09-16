class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = "*"
        self.generate_suffix_trie(string)

    def generate_suffix_trie(self, string):
        node = self.root
        for i in range(len(string)):
            for j in range(i, len(string)):
                letter = string[j]
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[self.end_symbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter in node:
                node = node[letter]
            else:
                return False
        return self.end_symbol in node


if __name__ == '__main__':
    trie = SuffixTrie("babc")
    print(trie)
