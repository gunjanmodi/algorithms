class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

def has_cycle(head):
	fast, slow = head, head
	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			# return True
			return calculate_cycle(slow)
	return False

def calculate_cycle(slow):
	current = slow
	count = 0
	while True:
		current = slow.next
		count += 1
		if current == slow:
			break
	return count


if __name__ == '__main__':
	head = LinkedList(1)
	head.next = LinkedList(2)
	head.next.next = LinkedList(3)
	head.next.next.next = LinkedList(4)
	head.next.next.next.next = LinkedList(5)
	head.next.next.next.next.next = LinkedList(6)
	# print("Has Loop? ", has_cycle(head))
	head.next.next.next.next.next.next = head.next.next
	print("Has Loop? ", has_cycle(head))

