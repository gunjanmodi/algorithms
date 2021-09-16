def find_subsets(nums):
  list.sort(nums)
  subsets = []
  subsets.append([])
  start, end = 0, 0
  for i in range(len(nums)):
    start = 0
    if i > 0 and nums[i] == nums[i - 1]:
      start = end + 1
    end = len(subsets)
    for j in range(start, end):
      set1 = list(subsets[j])
      set1.append(nums[i])
      subsets.append(set1)


  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()