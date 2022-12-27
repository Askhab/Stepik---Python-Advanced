list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for arr in list1:
    for i in arr:
        maximum = max(maximum, i)

print(maximum)
