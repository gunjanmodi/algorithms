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


def main(grid, word):
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            explore(i, j, 0, grid, word, result, 'all')
    return [[-1, -1]] if result == [] else result


def explore(i, j, k, grid, word, result, current_direction):

    letter = grid[i][j]
    if letter != word[k]:
        return False
    elif current_direction == 'all':
        neighbours = tuple(get_neighbours(i, j, grid, 'all').values())
        for neighbour in neighbours:
            is_possible = explore(neighbour[0], neighbour[1], k+1, grid, word, result, neighbour[2])
            if is_possible:
                result.append([i, j])
    else:
        if k == len(word) - 1:
            return True
        current_neighbour = get_neighbours(i, j, grid, current_direction).get(current_direction)
        if current_neighbour:
            return explore(current_neighbour[0], current_neighbour[1], k+1, grid, word, result, current_neighbour[2])


def get_neighbours(i, j, grid, direction):
    neighbours = {}
    if j < len(grid[i]) - 1 and direction in ['all', 'right']:
        neighbours["right"] = [i, j+1, "right"]
    if j > 0 and direction in ['all', 'left']:
        neighbours["left"] = [i, j - 1, "left"]
    if i > 0 and direction in ['all', 'top']:
        neighbours["top"] = [i - 1, j, 'top']
    if i < len(grid) - 1 and direction in ['all', 'bottom']:
        neighbours["bottom"] = [i + 1, j, "bottom"]
    if i > 0 and j < len(grid[i]) - 1 and direction in ['all', 'top-right']:
        neighbours["top-right"] = [i - 1, j + 1, 'top-right']
    if i > 0 and j > 0 and direction in ['all', 'top-left']:
        neighbours["top-left"] = [i - 1, j - 1, 'top-left']
    if i < len(grid) - 1 and j > 0 and direction in ['all', 'bottom-left']:
        neighbours["bottom-left"] = [i + 1, j - 1, "bottom-left"]
    if i < len(grid) - 1 and j < len(grid[i]) - 1 and direction in ['all', 'bottom-right']:
        neighbours["bottom-right"] = [i + 1, j + 1, "bottom-right"]
    return neighbours






# Test case 1: Normal or Given input
print(main([['a','b','a','b'], ['a','b','e','b'], ['e','b','e','b']], "abe"))
# Test case 2: Normal or Given input
print(main([['a','b','c'], ['a', 'b', 'c'], ['g', 'h', 'c']], "abc"))
# Test case 3: Normal or Given input
# print(main([['a', 'b', 'a', 'e', 'b', 'e', 'e', 'e', 'c', 'c'],
#             ['a', 'b', 'e', 'c', 'b', 'd', 'e', 'c', 'a', 'd'],
#             ['e', 'c', 'c', 'c', 'c', 'a', 'd', 'a', 'c', 'b'],
#             ['e', 'e', 'a', 'd', 'd', 'd', 'c', 'b', 'b', 'b'],
#             ['b', 'd', 'b', 'a', 'c', 'a', 'b', 'b', 'd', 'd'],
#             ['c', 'c', 'c', 'd', 'a', 'e', 'a', 'c', 'e', 'b']], "bed"))

# Test case 4: Negative
print(main([['c'], ['b'], ['a'], ['c'], ['e'], ['a']], "ead"))
# Test case 5: Empty
# print(main())
# Test case 6: Too long
# print(main())
# Test case 7
# Test case 8
# Test case 9