def commonElements(ar1, ar2, ar3):
    result = []
    i, j, k = 0, 0, 0

    while i < len(ar1) and j < len(ar2) and k < len(ar3):
        if ar1[i] == ar2[j] and ar2[j] == ar3[k]:
            result.append(ar1[i])
            i += 1
            j += 1
            k += 1


        elif ar1[i] < ar2[j]:
            i += 1

        elif ar2[j] < ar3[k]:
            j += 1

        else:
            k += 1

    return result


print(commonElements([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]))