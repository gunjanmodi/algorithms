def do_union(list1, list2):
	ref_dict = {}
	result = []
	for num in list1:
		current = ref_dict.get(num, 0)
		ref_dict[num] = current + 1
	for num in list2:
		current = ref_dict.get(num, 0)
		ref_dict[num] = current + 1
	for key, value in ref_dict.items():
		if value >= 1:
			result.append(key)
	print(result)
	return result

if __name__ == '__main__':
	list1 = [85, 25, 1, 32, 54, 6, 54]
	list2 = [98, 1, 90, 54]
	do_union(list1, list2)