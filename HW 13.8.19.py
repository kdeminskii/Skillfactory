tickets = int(input("Введите количество билетов: "))
age = int(input("Введите ваш возраст: "))
m_price = 990
b_price = 1390
if age < 18:
    print("Вам доступны бесплатные билеты!")
elif 18 <= age <= 25:
    if tickets > 3:
        print("Стоимость билета:", (m_price * tickets - m_price * tickets * 0.1), "руб.")
    else:
        print("Стоимость билета:", (m_price * tickets), "руб.")
elif age > 25:
    if tickets > 3:
        print("Стоимость билета:", (b_price * tickets - b_price * tickets * 0.1), "руб.")
    else:
        print("Стоимость билета:", (b_price * tickets), "руб.")