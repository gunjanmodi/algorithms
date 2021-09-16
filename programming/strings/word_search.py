"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O()
# Space: O()


def main(board, word):
    result = []
    visited = []
    for row in board:
        visited.append([False] * len(row))
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, 0, board, word, result, visited)
    return True if len(result) > 0 else False


def get_neighbours(i, j, board):
    neighbours = {}
    if j < len(board[i]) - 1:
        neighbours["right"] = [i, j + 1, "right"]
    if j > 0:
        neighbours["left"] = [i, j - 1, "left"]
    if i > 0:
        neighbours["top"] = [i - 1, j, 'top']
    if i < len(board) - 1:
        neighbours["bottom"] = [i + 1, j, "bottom"]
    if i > 0 and j < len(board[i]) - 1:
        neighbours["top-right"] = [i - 1, j + 1, 'top-right']
    if i > 0 and j > 0:
        neighbours["top-left"] = [i - 1, j - 1, 'top-left']
    if i < len(board) - 1 and j > 0:
        neighbours["bottom-left"] = [i + 1, j - 1, "bottom-left"]
    if i < len(board) - 1 and j < len(board[i]) - 1:
        neighbours["bottom-right"] = [i + 1, j + 1, "bottom-right"]
    return neighbours


def explore(i, j, k, board, word, result, visited):
    if not visited[i][j]:
        visited[i][j] = True
        if k == len(word):
            return result
        letter = board[i][j]
        if letter != word[k]:
            return False
        else:
            neighbours = tuple(get_neighbours(i, j, board).values())
            if not neighbours and letter == word:
                result.append([i, j])
                return result
            else:
                for neighbour in neighbours:
                    explore(neighbour[0], neighbour[1], k + 1, board, word, result, visited)
                    if k == len(word) - 1:
                        result.append([i, j])
                        return result

print(main([["a", "b"]], "ba"))
print(main([["a"]], "a"))
print(main([["a"]], "ab"))
print(main([["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]], "ABCCED"))
print(main([["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]], "ABCB"))
