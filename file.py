def quickSort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(1, n):
        ii = i
        while(ii > 0 and arr[ii] < arr[ii - 1]):
            temp = arr[ii - 1]
            arr[ii - 1] = arr[ii]
            arr[ii] = temp
            ii -= 1
    return arr


a = [5, 2, 3, 1]
print(quickSort(a))

a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 5, 5, 6, 6, 0, -1]
print(quickSort(a))