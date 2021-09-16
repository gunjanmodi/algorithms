def spiral_traverse(mattrix):
	result = []
	start_row, end_row = 0, len(mattrix) - 1
	start_col, end_col = 0, len(mattrix[0]) - 1



	while start_row < end_row and start_col < end_col:
		# print(f"start_row - {start_row}")
		# print(f"end_row - {end_row}")
		# print(f"start_col - {start_col}")
		# print(f"end_col - {end_col}")
		for i in range(start_col, end_col + 1):
			result.append(mattrix[start_row][i])
		for j in range(start_row + 1, end_row + 1):
			result.append(mattrix[j][end_col])
		for k in reversed(range(start_col, end_col)):
			result.append(mattrix[end_row][k])
		for l in reversed(range(start_row + 1, end_row)):
			result.append(mattrix[l][start_col])
		start_row += 1
		end_row -= 1
		start_col += 1
		end_col -= 1


if __name__ == '__main__':
	mattrix = [ [1,  2,  3,  4],
				[12, 13, 14, 5],
				[11, 16, 15, 6],
				[10, 9,  8,   7]
			  ]
	spiral_traverse(mattrix)
