money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = salary - spend
while money_capital >= spend:
    spend = spend * (1 + increase)
    money_capital += delta
    month += 1

# TODO Оформить решение

print(month)
