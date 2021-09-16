"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(jobs):
    deadline, profit = 1, 2
    jobs.sort(key=lambda x: x[profit], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[deadline])[deadline]
    slots = [-1] * max_deadline
    visited = [False] * max_deadline
    max_profit = 0

    # latest_possible_slot = jobs[0][deadline] - 1
    # slots[latest_possible_slot] = jobs[0][profit]
    # max_profit = jobs[0][profit]
    # max_deadline -= 1
    for i in range(len(jobs)):
        job = jobs[i]
        if visited[job[deadline] - 1]:
            continue
        j = get_latest_possible_slot(slots, job[deadline], visited)
        # for j in range(min(max_deadline - 1, job[deadline] - 1), -1, -1):
        if visited[j] is False:
            visited[j] = True
            slots[j] = job[profit]
            max_profit += job[profit]
            max_deadline -= 1
            if max_deadline == 0:
                break
    return max_profit


def get_latest_possible_slot(slots, deadline, visited):
    i = 0
    while i < len(slots):
        if slots[deadline - 1] == -1:
            return deadline - 1
        if slots[i] == -1:
            return i
        i += 1
    return -1



# Test cases: Normal1, Normal2, Normal3, Negativ e, Empty, Too long
print(main([(1, 2, 100), (2, 1, 50), (3, 2, 10), (4, 1, 20), (5, 3, 30)])) # 180
print(main([(1,2,100),(2,1,19),(3,2,27), (4,1,25), (5,1,15)])) # 127
print(main([(1, 4, 70), (2, 1, 80), (3, 1, 30), (4, 1, 100)])) # 170
print(main([(1, 2, 50), (2, 2, 60), (3, 3, 20), (4, 3, 30)])) # 140
print(main([(1,4,20),(2,1,10),(3,1,40),(4,1,30)])) # 60
