digit = input()

if len(digit) <= 5:
    digit = digit[::-1]
    print(int(digit))

if len(digit) > 5:
    first_part = digit[0: -5]
    second_part = digit[-1:-6:-1]
    print(f"{first_part}{str(second_part)}")
