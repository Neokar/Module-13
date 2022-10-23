tickets = int(input("Введите количество билетов: "))
if tickets >= 1:
    L = [int(input("Введите возраст посетителя ")) for i in range(tickets)]
    data = []
    for item in L:
        if item < 18:
            price = 0
            data.append(price)
        elif 18 <= item < 25:
            price = 990
            data.append(price)
        elif item >= 25:
            price = 1390
            data.append(price)
    if tickets > 3:
        final_price = (sum(data) - (sum(data) / 10))
    else:
        final_price = sum(data)
    print(int(final_price), "руб.")
else:
    print("Вы ввели некорректное колличество билетов")
