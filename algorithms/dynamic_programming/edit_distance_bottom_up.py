def min_distance(word1, word2):
	memo = {}
	return min_distance_helper(word1, word2, 0, 0, memo)


def min_distance_helper(word1, word2, i, j, memo):
	if i == len(word1) and j == len(word2):
		return 0
	if i == len(word1):
		return len(word2) - j
	if j == len(word2):
		return len(word1) -i

	if (i, j) not in memo:
		if word1[i] == word2[j]:
			answer = min_distance_helper(word1, word2, i + 1, j + 1, memo)
		else:
			insert = 1 + min_distance_helper(word1, word2, i, j + 1, memo)
			delete = 1 + min_distance_helper(word1, word2, i + 1, j, memo)
			replace = 1 + min_distance_helper(word1, word2, i + 1, j + 1, memo)
			answer =  min(insert, delete, replace)
		memo[(i, j)] = answer

	return memo[(i, j)]


print(min_distance("horse", "ros"))
print(min_distance("intention", "execution"))