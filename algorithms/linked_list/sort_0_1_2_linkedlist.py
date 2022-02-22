def segregate(self, head):
    count = [0, 0, 0]
    node = head
    while node:
        count[node.data] += 1
        node = node.next

    node = head
    current_pointer = 0
    while node:
        if count[current_pointer] == 0:
            current_pointer += 1
        else:
            node.data = current_pointer
            count[current_pointer] -= 1
            node = node.next
    return head