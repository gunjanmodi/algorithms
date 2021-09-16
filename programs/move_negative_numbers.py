def move_negative_numbers(array, n):
	j = 0
	for i in range(len(array)):
		if array[i] < 0:
			array[j], array[i] = array[i], array[j]
			j += 1
	return array


if __name__ == '__main__':
	array = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
	n = len(array)
	move_negative_numbers(array, n)