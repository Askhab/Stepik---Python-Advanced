mass, height = float(input()), float(input())

body_mass_index = mass / (height ** 2)

if 18.5 <= body_mass_index <= 25:
    print("Оптимальная масса")
elif 18.5 > body_mass_index:
    print("Недостаточная масса")
elif body_mass_index > 25:
    print("Избыточная масса")
