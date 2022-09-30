day_of_week=input("Введите число: ")

if (5< int(day_of_week) <=7):
    print("Выходной")
else :
    if (int(day_of_week)>7 or int(day_of_week)==0):
        print("error")

    else:
        print("Рабочий")