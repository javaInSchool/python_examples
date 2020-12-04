#https://www.e-olymp.com/uk/problems/10168

import math
fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису

n = int(fin.readline())         #для читання 1 числа з файлу
#n, m = map(int, fin.readline().split())  #прочитати 2 числа
s = 0.0
for x in range(1,(n+1)):
    s = s + 1/math.pow(x,2)
fout.write(str("{:.6f}".format(s)))

fin.close()         #закрити файл
fout.close()        #закрити файл