def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    final_words = {}
    visited = [[ False for value in row] for row in board]

    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, final_words)
    return list(final_words.keys())

def explore(i, j, board, trie_node, visited, final_words):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trie_node:
        return
    visited[i][j] = True
    trie_node = trie_node[letter]
    if "*" in trie_node:
        final_words[trie_node['*']] = True
    neighbours = get_neighbours(i, j, board)
    for neighbour in neighbours:
        explore(neighbour[0], neighbour[1], board, trie_node, visited, final_words)
    visited[i][j] = False


def get_neighbours(i, j, board):
    neighbours = []
    if i > 0 and j > 0:
        neighbours.append([i-1, j-1])
    if i > 0 and j < len(board[0]) - 1:
        neighbours.append([i-1, j+1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbours.append([i+1, j+1])
    if i < len(board) - 1 and j > 0:
        neighbours.append([i+1, j-1])
    if i > 0:
        neighbours.append([i-1, j])
    if i < len(board) - 1:
        neighbours.append([i+1, j])
    if j > 0:
        neighbours.append([i, j-1])
    if j < len(board[0]) - 1:
        neighbours.append([i, j+1])
    return neighbours
    


		
class Trie:
	def __init__(self):
		self.root = {}
		self.end_symbol = '*'
		
	def add(self, word):
		node = self.root
		for letter in word:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.end_symbol] = word


if __name__ == '__main__':
    board = [
        ["F", "a", "t", "e", "*", "d", "o", "e", "s", "*", "n", "o", "t"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"],
        Fate does not stop at the lovers meeting and also plays a part as Romeo misses the messenger Balthasar. This one incident alone leads to Romeo believing Juliet is dead and drives him to his own suicide.
    ]

    words = [
        "this",
        "is",
        "not",
        "a",
        "simple",
        "boggle",
        "board",
        "test",
        "REPEATED",
        "NOTRE-PEATED"
    ]
    boggleBoard(board, words) 