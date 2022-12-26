random_numbers = input().split(" ")
swapped_numbers = ""

while len(random_numbers) != 0:
    arr = []
    if len(random_numbers) != 1:
        for j in range(2):
            arr.append(random_numbers[0])
            del random_numbers[0]

        arr = arr[::-1]

        for i in arr:
            swapped_numbers += f"{i} "
        arr.clear()
    else:
        swapped_numbers += random_numbers[0]
        del random_numbers[0]

print(swapped_numbers)
