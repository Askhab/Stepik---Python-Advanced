virus = ["a", "n", "t", "o", "n"]
num = int(input())
text_list = []
final = ""

for _ in range(num):
    text_list.append(input())

for i in range(len(text_list)):
    amount = 0
    last_index = 0
    for j in virus:
        for l in range(last_index, len(text_list[i])):
            if text_list[i][l] == j:
                last_index = l + 1
                amount += 1
                break
    if amount == 5:
        final += f"{i + 1} "

print(final.rstrip())
