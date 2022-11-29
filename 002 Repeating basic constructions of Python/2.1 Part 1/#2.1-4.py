from math import ceil

text = input()

summary = round(len(text) * 0.60, 2)
summary_int = int(summary)
summary_float = int((summary * 100) % 100)

print(f"{summary_int} р. {summary_float} коп.")
