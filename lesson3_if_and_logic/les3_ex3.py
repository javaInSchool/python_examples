#https://www.e-olymp.com/uk/problems/2391
fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису

#n = int(fin.readline())         #для читання 1 числа з файлу
a, b, n = map(int, fin.readline().split())
if n % 60 == 0:     # 120 % 60 = 0, 132 % 60 = 12
    n1 = 0
else:
    n1 = 1
if n != 0:
    fout.write( str( (n//60+n1)*b+a ) )  # (132 // 60 + 1) * 10 + 5 = 35
else:
   fout.write(str(0))

fin.close()         #закрити файл
fout.close()        #закрити файл


