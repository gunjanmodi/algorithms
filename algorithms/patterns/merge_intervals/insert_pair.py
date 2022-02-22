def insert_pair(intervals, new_interval):
    merged = []
    i = 0
    start, end = 0, 1
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] < new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = min(intervals[i][end], new_interval[end])
        i += 1

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
        
    print(merged)
    return merged


if __name__ == '__main__':
    insert_pair([[1, 3], [5, 7], [8, 12]], [4, 6])