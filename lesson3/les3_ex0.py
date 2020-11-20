#Булеві змінні, true/false

b = 5 > 4  # true
print(b)
a = 10 == 6 #   = - означає присвоїти, == - порівняти, != - не дорівнює
print(a)
c = 10 != 6
print(c)

#оператор розгалуження if else, elif
myMoney = 500
price = 501
isOpen = True
if (myMoney >= price):
    print("Ураа, ми купуємо нову іграшку!")
    print("Скоріш додому грати.")
elif isOpen:
    print("Тоді підемо до кіно!")
else:
    print("Ну тоді погуляємо на вулиці!")

#логічні оператори
if (myMoney >= price and isOpen):
    print("Ура, підемо до кіно!")
else:
    print("Погуляємо на вулиці!")

isOpenSecond = True
if (isOpen or isOpenSecond):
    print("Ура, підемо до кіно!")
else:
    print("Погуляємо на вулиці!")

print( not(isOpenSecond) )
