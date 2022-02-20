def steps_by_knight(KnightPos, TargetPos, N):
    dp = [[0 for i in range(N)] for j in range(N)];
    visited = set()
    current = 0
    return dfs(KnightPos[0], KnightPos[1], TargetPos, N, current, dp, visited)
	
	
	
def dfs(i, j, target, n, current, dp, visited):

    if i == target[0] and j == target[1]:
        return dp[i][j]

    if i < 1 or j < 1 or i >= n or j >= n:
        return 0

    if (i, j) in visited:
        return dp[i][j]

    visited.add((i, j ))
    
    dp [i][j] = 1 + min(
        dfs(i + 2, j + 1, target, n, current, dp, visited),
        dfs(i + 2, j - 1, target, n, current, dp, visited),
        dfs(i - 2, j + 1, target, n, current, dp, visited),
        dfs(i - 2, j - 1, target, n, current, dp, visited),
        dfs(i + 1, j + 2, target, n, current, dp, visited),
        dfs(i + 1, j - 2, target, n, current, dp, visited),
        dfs(i - 1, j + 2, target, n, current, dp, visited),
        dfs(i - 1, j - 2, target, n, current, dp, visited)
    )
    return dp[i][j]

if __name__ == '__main__':
    print(steps_by_knight([4, 5], [1, 1], 8))
