list_of_numbers = input().split(" ")
s = ""

list_of_numbers.insert(0, list_of_numbers[-1])
del list_of_numbers[-1]

for i in range(0, len(list_of_numbers)):
    if i != len(list_of_numbers) - 1:
        s += f"{list_of_numbers[i]} "
    else:
        s += list_of_numbers[i]

print(s)
