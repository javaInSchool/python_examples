step = 0
tired = True
badweather = False
while step < 10000: #якщо умова - True,  тоді виконуємо команди
    print(step)
    if tired == True and step == 9900:
        print('потрібно відпочити')
        tired = False
        print('відпочили - вперед!')
        continue
    else:
        step = step + 1
print('Ура піднялись!')