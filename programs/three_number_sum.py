def three_number_sum(array, target_sum):
    array.sort()
    result = []
    for i in range(len(array)):
        left_idx = i + 1
        right_idx = len(array) - 1
        while left_idx < right_idx:
            current_sum = array[i] + array[left_idx] + array[right_idx]
            if current_sum < target_sum:
                left_idx += 1
            elif current_sum > target_sum:
                right_idx -= 1
            else:
                result.append([ array[i], array[left_idx], array[right_idx] ])
                left_idx += 1
                right_idx -= 1
    return result


def triplet_sum_close_to_target(arr, target_sum):
  array = arr
  array.sort()
  closest_sum = float("inf")
  smallest_triplet = []
  for i in range(len(array)):
      left_idx = i + 1
      right_idx = len(array) - 1
      while left_idx < right_idx:
          current_sum = array[i] + array[left_idx] + array[right_idx]
          if abs(target_sum - current_sum) < abs(target_sum - closest_sum):
              closest_sum = current_sum
          if current_sum == target_sum:
              return current_sum
          if current_sum < target_sum:
              left_idx += 1
          elif current_sum > target_sum:
              right_idx -= 1
  return closest_sum


def triplets_with_smaller_sum(arr, target_sum):
    target = target_sum
    count = 0
    arr.sort()
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        while left == i and :
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum < target:
                count += 1
                left += 1
            else:
                right -= 1
                
    return count



if __name__ == '__main__':
    # output = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    # output = triplet_sum_close_to_target([-2, 0, 1, 2], 2)
    output = triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5)
    print(output)