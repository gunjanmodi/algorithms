"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(arrival, departure):
    mapping = list(zip(arrival, departure))
    mapping.sort(key=lambda x: x[0])
    min_req_platforms = 1
    available_platforms = 0
    arr, dept = 0, 1
    previous = mapping[0]
    platform_queues = {previous[arr]: previous}
    for i in range(1, len(mapping)):
        current = mapping[i]
        for key in list(platform_queues):
            train = platform_queues[key]
            if train[dept] < current[arr]:
                platform_queues.pop(key)
                available_platforms += 1
        if available_platforms == 0:
            min_req_platforms += 1
        platform_queues[current[arr]] = current
        available_platforms -= 1
        if available_platforms < 0:
            available_platforms = 0
    return min_req_platforms


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(['0900', '0940', '0950', '1100', '1500', '1800'],
           ['0910', '1200', '1120', '1130', '1900', '2000']))