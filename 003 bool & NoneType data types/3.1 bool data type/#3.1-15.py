def func(n1, n2):
    return n1 % n2 == 0


num1, num2 = int(input()), int(input())

if func(num1, num2):
    print("делится")
else:
    print("не делится")
