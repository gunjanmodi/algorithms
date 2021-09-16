def search_next_letter(letters, key):
  left = 0
  right = len(letters) - 1
  if key < letters[left] or key > letters[right]:
    return letters[left]
  while left <= right:
      mid = (left + right) // 2
      if key < letters[mid]:
        right = mid - 1
      else:
        left = mid + 1
  return letters[left % len(letters)]

def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()