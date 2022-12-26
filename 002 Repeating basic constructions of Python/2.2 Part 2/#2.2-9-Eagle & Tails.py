text = input().upper()
amount = 0
num = 0

for i in range(0, len(text)):
    letter = ""
    if letter == "P" or letter == "" and text[i] == "Р":
        letter = "P"
        num += 1
    if text[i] == "О" or i == len(text) - 1:
        if num > amount:
            amount = num
        num = 0

print(amount)
