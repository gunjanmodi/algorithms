def smallest_subarray_with_given_sum(array, desired_sum):
  window_size = 1
  while window_size < len(array):
    window_start = 0
    current_sum = 0
    for window_end in range(len(array)):
      current_sum += array[window_end]
      if window_end >= window_size - 1:
        if current_sum >= desired_sum:
          return window_size
        current_sum -= array[window_start]
        window_start += 1
    window_size += 1
  return -1

if __name__ == '__main__':
	output = smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7)
	print(output)