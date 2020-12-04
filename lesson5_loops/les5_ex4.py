# програмв знаходження суми всіх чисел зі списку
# список чисел
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# початкове значення суми
sum = 0

# перебираємо всі числа
for val in numbers:
	sum = sum+val
#1 крок: val = 6
#2 крок: sum = 0 + 6
#3 крок: val = 5
#4 крок: sum = 6 + 5
# ...
print("Сума: ", sum)


# програма, що відображає оцінки учня зі списку
student_name = 'James'

marks = {'James': 90, 'Oleh': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('Не знайдено жодного запису з цим ім\'ям')