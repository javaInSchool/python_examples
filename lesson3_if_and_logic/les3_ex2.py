#https://www.e-olymp.com/uk/problems/9937

import math
fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису

#a = int(fin.readline())         #для читання 1 числа з файлу
n, m = map(int, fin.readline().split())  #прочитати 2 числа
mini = int(math.pow(10, n-1))
maxi = int(math.pow(10, n))-1
#print(mini, maxi)
#print(m)
if (m >= mini and m <= maxi):
    result = maxi - m
elif(m > maxi):
    result = 0
else:
    result = maxi - mini + 1
#print(result)
fout.write(str(result))

fin.close()         #закрити файл
fout.close()        #закрити файл