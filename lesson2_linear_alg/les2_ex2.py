#Радіус кола та кільце
import math

fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису

#a = int(fin.readline())         #для читання 1 числа з файлу
s, r1 = map(float, fin.readline().split())  #прочитати 2 дробових числа
print(s)
print(r1)

r2 = math.sqrt((math.pi*r1*r1-s)/math.pi)

fout.write(str("{0:.2f}".format(round(r2,2))))

fin.close()         #закрити файл
fout.close()        #закрити файл