def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [intervals[0]]
    j = 0
    start, end = 0, 1
    for i in range(1, len(intervals)):
        current = intervals[i]
        previous = merged_intervals[j]
        if current[start] <= previous[end]:
            merged_intervals[j][start] = previous[start]
            merged_intervals[j][end] = max(current[end], previous[end])
        else:
            merged_intervals.append(current)
            j += 1

    return merged_intervals


# print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[4,5]]))
# print(merge([[1,4],[2,3]]))
print(merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))
