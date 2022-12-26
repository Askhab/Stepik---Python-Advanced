numbers_amount = int(input())
numbers_list = []
result = "НЕТ"

for _ in range(numbers_amount):
    number = int(input())
    numbers_list.append(number)

numbers_product = int(input())

for i in range(len(numbers_list) - 1):
    for j in range(i + 1, len(numbers_list)):
        if numbers_list[i] * numbers_list[j] == numbers_product:
            result = "ДА"
            break

print(result)
