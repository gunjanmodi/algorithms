def cyclic_rotation_by_one(array):
	last_val = array[-1]
	for i in reversed(range(len(array))):
		array[i] = array[i - 1]
	return array

if __name__ == '__main__':
	array = [1, 2, 3, 4, 5]
	cyclic_rotation_by_one(array)