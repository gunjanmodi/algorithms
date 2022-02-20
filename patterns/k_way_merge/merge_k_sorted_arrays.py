from __future__ import print_function
from heapq import *


# class ListNode:
#   def __init__(self, value):
#     self.value = value
#     self.next = None

#   # used for the min-heap
#   def __lt__(self, other):
#     return self.value < other.value


def merge_lists1(lists):
	minHeap = []

	# put the root of each list in the min heap
	for root in lists:
		if root is not None:
			heappush(minHeap, root)

	# take the smallest(top) element form the min-heap and add it to the result
	# if the top element has a next element add it to the heap
	resultHead, resultTail = None, None
	while minHeap:
		node = heappop(minHeap)
		if resultHead is None:
			resultHead = resultTail = node
		else:
			resultTail.next = node
			resultTail = resultTail.next

		if node.next is not None:
			heappush(minHeap, node.next)

	return resultHead


def merge_lists(lists):
	min_heap = []
	for l in range(len(lists)):
		heappush(min_heap, (lists[l][0], l, 0))

	result = []
	while min_heap:
		num, lists_index, current_index = heappop(min_heap)
		result.append(num)
		next_index = current_index + 1
		if next_index < len(lists[lists_index]):
			heappush(min_heap,  (lists[lists_index][next_index], lists_index, next_index) )
	return result

def main():
	# l1 = ListNode(2)
	# l1.next = ListNode(6)
	# l1.next.next = ListNode(8)

	# l2 = ListNode(3)
	# l2.next = ListNode(6)
	# l2.next.next = ListNode(7)

	# l3 = ListNode(1)
	# l3.next = ListNode(3)
	# l3.next.next = ListNode(4)

	l1 = [2, 6, 8]
	l2 = [3, 6, 7]
	l3 = [1, 3, 4]
	result = merge_lists([l1, l2, l3])
	print("Here are the elements form the merged list: ", end='')
	while result is not None:
		print(str(result.value) + " ", end='')
		result = result.next


main()



from heapq import *
def mergeSortedArrays(arrays):
	lists = arrays
	min_heap = []
	for l in range(len(lists)):
		heappush(min_heap, (lists[l][0], l, 0))
	
	result = []
	while min_heap:
		num, lists_index, current_index = heappop(min_heap)
		result.append(num)
		next_index = current_index + 1
		if next_index < len(lists[lists_index]):
			heappush(min_heap,  (lists[lists_index][next_index], lists_index, next_index) )
	return result
