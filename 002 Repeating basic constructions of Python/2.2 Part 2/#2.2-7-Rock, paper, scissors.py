timur_choice = input()
ruslan_choice = input()

if timur_choice == ruslan_choice:
    print("ничья")
elif timur_choice == "ножницы" and ruslan_choice == "бумага":
    print("Тимур")
elif timur_choice == "бумага" and ruslan_choice == "камень":
    print("Тимур")
elif timur_choice == "камень" and ruslan_choice == "ножницы":
    print("Тимур")
else:
    print("Руслан")

