"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main_naive(matrix):
    result = 0
    while True:
        changed = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 2:
                    changed = explore(matrix, i, j)
        result += 1
        if not changed:
            break

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                return -1
    return result


def explore(matrix, i, j):
    changed = False
    if i > 0 and matrix[i - 1][j] == 1:
        matrix[i - 1][j] = 2
        changed = True
    if i + 1 < len(matrix) and matrix[i + 1][j] == 1:
        matrix[i + 1][j] = 2
        changed = True
    if j > 0 and matrix[i][j - 1] == 1:
        matrix[i][j - 1] = 2
        changed = True
    if j + 1 < len(matrix[i]) and matrix[i][j + 1] == 1:
        matrix[i][j + 1] = 2
        changed = True
    return changed


from collections import deque
class BFSSolution:
    def main(self, matrix):
        queue = deque()
        rows = len(matrix)
        columns = len(matrix[0])
        fresh_count = 0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 2:
                    queue.append((i, j))
                elif matrix[i][j] == 1:
                    fresh_count += 1

        minutes_passed = 0
        while len(queue) > 0 and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                queue, fresh_count = self.explore_neighbours(matrix, queue, fresh_count)
        return minutes_passed

    def explore_neighbours(self, matrix, queue, fresh_count):
        i, j = queue.popleft()
        if i > 0 and matrix[i - 1][j] == 1:
            matrix[i - 1][j] = 2
            fresh_count -= 1
            queue.append((i - 1, j))

        if i + 1 < len(matrix) and matrix[i + 1][j] == 1:
            matrix[i + 1][j] = 2
            fresh_count -= 1
            queue.append((i + 1, j))
        if j > 0 and matrix[i][j - 1] == 1:
            matrix[i][j - 1] = 2
            fresh_count -= 1
            queue.append((i, j - 1))
        if j + 1 < len(matrix[i]) and matrix[i][j + 1] == 1:
            matrix[i][j + 1] = 2
            fresh_count -= 1
            queue.append((i, j + 1))
        return queue, fresh_count


    def leet(self, grid):
        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1

        # number of columns
        cols = len(grid[0])

        # keep track of fresh oranges
        fresh_cnt = 0

        # queue with rotten oranges (for BFS)
        rotten = deque()

        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1

        # keep track of minutes passed.
        minutes_passed = 0

        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    # update the fresh oranges count
                    fresh_cnt -= 1

                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2

                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
bfs_solution = BFSSolution()
# print(bfs_solution.main([[2,1,1], [1,1,0], [0, 1, 1]]))
# print(bfs_solution.leet([[2,1,1], [1,1,0], [0, 1, 1]]))
print(bfs_solution.main([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))
print(bfs_solution.leet([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))
# print(bfs_solution.main([[2, 2, 0, 1]]))
