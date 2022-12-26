number_of_dots = int(input())
arr = []
first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0

for i in range(number_of_dots):
    arr.append(input().split(" "))

for j in arr:
    if int(j[0]) == 0 or int(j[1]) == 0:
        continue
    elif int(j[0]) > 0 and int(j[1]) > 0:
        first_quarter += 1
    elif int(j[0]) < 0 and int(j[1]) > 0:
        second_quarter += 1
    elif int(j[0]) < 0 and int(j[1]) < 0:
        third_quarter += 1
    elif int(j[0]) > 0 and int(j[1]) < 0:
        fourth_quarter += 1

print(f"Первая четверть: {first_quarter}")
print(f"Вторая четверть: {second_quarter}")
print(f"Третья четверть: {third_quarter}")
print(f"Четвертая четверть: {fourth_quarter}")
