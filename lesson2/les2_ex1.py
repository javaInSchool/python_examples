#Друзі Степана

fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису

a = int(fin.readline())         #для читання 1 числа з файлу
#a, b = map(int, fin.readline().split())  #прочитати 2 числа

fout.write(str(a-1)) # str - String, текстовий рядок

fin.close()         #закрити файл
fout.close()        #закрити файл