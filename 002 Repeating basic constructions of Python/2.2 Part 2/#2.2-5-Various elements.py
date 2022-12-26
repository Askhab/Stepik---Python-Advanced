list_of_numbers = input().split(" ")
unique = []

for i in list_of_numbers:
    if i in unique:
        continue
    else:
        unique.append(i)

print(len(unique))
