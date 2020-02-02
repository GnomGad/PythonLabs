
import sys
newpath = sys.path.append(sys.path[0].replace("Lab1",""))
from MyTools import ReadCSV

def Ex1():
    ReadCSV(num=1)
    try:
        money = float(input("Ввод: "))
        if money < 0:
            raise Exception("Ввод отрицательного числа")
        rub = money//1
        print(int(rub),"рублей")
        print(round((money-rub)*100),"копеек")
    except Exception as e:
        print("ERROR ", e)

def Ex2():
    ReadCSV(num=2)
    array1 = [1,4,4,6]
    array2 = list(range(10))
    Ex2_1(array1)
    Ex2_1(array2)
    
def Ex2_1(x):
    flag = True
    past = x[0]
    for i in x:
        if past<i:
            past = i
        elif past==i and flag:
            flag = False
        elif past>=i and not flag:
            print("False")
            flag = True
            break
    if not flag:
        print("True")

def Ex3():
    ReadCSV(num=3)
    goodnum = "1222489822223131"
    badnum = "123221321321311"
    try:
        snumber = input("Ввод: ")
        snumber = snumber.replace(" ","")
        number = int(snumber)
        if len(str(number)) != 16:
            s = "Вы ввели ",len(str(number)),"цифр вместо 16"
            raise Exception(s)
        count = 1
        s = ""
        for i in str(number):
            if count == 5 or count ==9 or count == 13:
                s=s+" "
            if count <= 4 or count>=13:
                s = s+ i
            else:
                s = s+"*"
            count+=1
        print(s)
    except Exception as e:
        print("ERROR ", e)    

def Ex4():
    stroka = "seseasdqd sadasd sadas s adqwdqwdwdqw asddqqd as qqqq wqesad reqwes"
    arr = stroka.split(" ")
    array = []
    flag = True
    for i in arr:
        array.append(len(i))
    array.sort(reverse=True)
    for i in range(12,0,-1):
        if flag and i>7:
            print("Больше 7")
            flag = False
        elif i>=4 and i<=7 and not flag:
            print("Меньше 7 и больше 4")
            flag =True
        elif i<4 and flag:
            print("Меньше 4")
            flag = False
        for j in arr:
            if i == len(j):
                print(j)
        
    

Ex4()