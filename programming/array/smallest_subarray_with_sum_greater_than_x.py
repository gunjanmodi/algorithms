def main(a, x):
    min_count = float('inf')
    for i in range(len(a)):
        current_count = 1
        current_total = a[i]
        if current_total > x:
            return 1
        for j in range(i + 1, len(a)):
            current_total += a[j]
            current_count += 1
            if current_total > x:
                min_count = min(min_count, current_count)
                break
    return min_count

print(main([1, 4, 45, 6, 0, 19], 51))
print(main([1, 10, 5, 2, 7], 9))