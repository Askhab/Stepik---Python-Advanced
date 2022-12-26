timur_choice = input().lower()
ruslan_choice = input().lower()

if timur_choice == ruslan_choice:
    print("ничья")
elif timur_choice == "ножницы" and ruslan_choice == "бумага" or timur_choice == "ножницы" and ruslan_choice == "ящерица":
    print("Тимур")
elif timur_choice == "бумага" and ruslan_choice == "камень" or timur_choice == "бумага" and ruslan_choice == "спок":
    print("Тимур")
elif timur_choice == "камень" and ruslan_choice == "ящерица" or timur_choice == "камень" and ruslan_choice == "ножницы":
    print("Тимур")
elif timur_choice == "ящерица" and ruslan_choice == "спок" or timur_choice == "ящерица" and ruslan_choice == "бумага":
    print("Тимур")
elif timur_choice == "спок" and ruslan_choice == "ножницы" or timur_choice == "спок" and ruslan_choice == "камень":
    print("Тимур")
else:
    print("Руслан")
