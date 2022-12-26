s = input()
arr = s.split(" ")
count = 0
ref = int(arr[0])

for i in range(1, len(arr)):
    if int(arr[i]) > ref:
        ref = int(arr[i])
        count += 1
    else:
        ref = int(arr[i])

print(count)
