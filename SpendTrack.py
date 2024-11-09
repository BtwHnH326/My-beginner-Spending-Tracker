#ТРЕКЕР ВИТРАТ

expenses={}
print("Привіт! Це трекер витрат на Python?")
while True:
    print("Що ти хочеш зробити?")
    print("1.Переглянути всі свої витрати.\n" "2.Вийти.")
    inputchoice=input("Вибирай!:")
    if inputchoice=="1":
        print(expenses)
        print("\nЩо ви хочете зробити?")
        print("\n1.Додати витрату""\n2.Видалити витрату""\n3.Переглянути сортування""\n4.Вийти")
        inputchoice_2=input("Вибирай!: ")
        if inputchoice_2 == "1":
            print("Окі!")
            expense_name = input("Впиши витрату!: ")
            expense_value = float(input("Впиши суму витрати: "))
            expenses[expense_name] = expense_value  # додаємо витрату з ім'ям та сумою
        elif inputchoice_2=="2":
            print("Окі!")
            input_del=input("Впишіть назву витрати яку ви хочете видалити: ")
            del expenses[input_del]
        elif inputchoice_2=="3":
            print("Окі!")
            print("Як саме ви хочете відсортувати список?")
            print("1.Від А до Я""\n2.Від Я до А""\n3.Від меншої ціни до більшої""\n4.Від більшої ціни до меншої")
            input_sorting=input("Вибирай!: ")
            if input_sorting=="1":
                sorted_by_lett_asc = dict(sorted(expenses.items()))
                print("Від A до Я за ключами:", sorted_by_lett_asc)
            elif input_sorting=="2":
                sorted_by_lett_desc = dict(sorted(expenses.items(), reverse=True))
            elif input_sorting == "3":
                sorted_by_val_asc = dict(sorted(expenses.items(), key=lambda x: x[1]))   # Сортуємо від меншої ціни до більшої (ТРЕБА РОЗІБРАТИ lambda!!!!)
                print("Від меншої ціни до більшої:", sorted_by_val_asc)
            elif input_sorting == "4":
                sorted_by_val_desc = dict(sorted(expenses.items(), key=lambda x: x[1], reverse=True))    # Сортуємо від більшої ціни до меншої (ТРЕБА РОЗІБРАТИ lambda!!!!)
                print("Від більшої ціни до меншої:", sorted_by_val_desc)
        elif inputchoice_2=="4":
            continue
        else:
            print("Ви ввели неправильну команду!")
            continue

    elif inputchoice=="2":
        print("Бувай!")
        break
    else:
        print("Ви ввели неправильну команду!")