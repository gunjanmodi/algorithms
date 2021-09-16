"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(computers_capacity, sequence):
    current_allocation = {}
    count = 0
    rejected = set()
    used = set()
    for customer in sequence:
        if customer in current_allocation:
            del current_allocation[customer]
            used.add(customer)
        elif len(current_allocation) >= computers_capacity and customer not in rejected and customer not in used:
            rejected.add(customer)
            count += 1
        elif customer not in current_allocation and len(current_allocation) < computers_capacity:
            current_allocation[customer] = True
            if customer in rejected:
                rejected.remove(customer)
                count -= 1
    return count




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print(main(2, "ABBAJJKZKZ"))
# print(main(3, "GACCBDDBAGEE"))
# print(main(3, "GACCBGDDBAEE"))
# print(main(1, "ABCBCADEED"))
# print(main(0, "ABCBCADEED"))
print(main(1, "ABCABCADEED"))
