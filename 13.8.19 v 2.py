PRICE_CHILD = 0
PRICE_STUDENT = 990
PRICE_FULL = 1390
YUONG_AGE = 18
OLD = 25

tickets = int(input("Введите количество билетов: "))
if tickets >= 1:
    L = [int(input("Введите возраст посетителя ")) for i in range(tickets)]
    sum_ALL = 0
    for item in L:
        if item < YUONG_AGE:
            sum_ALL += PRICE_CHILD
        elif YUONG_AGE <= item < OLD:
            sum_ALL += PRICE_STUDENT
        elif item >= OLD:
            sum_ALL += PRICE_FULL
    if tickets > 3:
        final_price = sum_ALL*0.9
    else:
        final_price = sum_ALL
    print(int(final_price), "руб.")
else:
    print("Вы ввели некорректное колличество билетов")
