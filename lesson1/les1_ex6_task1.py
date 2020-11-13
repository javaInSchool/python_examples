# https://www.e-olymp.com/uk/problems/8801
fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису, w - write

a = int(fin.readline())                     #для читання 1 числа з файлу
#int - перетворити символ на число
#a, b = map(int, fin.readline().split())    #прочитати 2 числа

fout.write(str(a+1))                        #додати числа та записати в файл суму
#str - перетворити число на рядок тексту
fin.close()         #закрити файл
fout.close()        #закрити файл