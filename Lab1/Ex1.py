
import sys
newpath = sys.path.append(sys.path[0].replace("Lab1",""))
from MyTools import ReadCSV

import random

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
        if snumber == basegood:
            snumber = goodnum
            print(snumber)
        elif snumber == basebad:
            snumber = badnum
            print(snumber)
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
        print("Возможные слова: ",basebad,basegood)    

def Ex4():
    ReadCSV(num=4)
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
        
    

def Ex5():
    ReadCSV(num=5)
    ABC = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    baseStroka = "город Донецк ,река Кальмиус"
    startStroka = input("Ввод текста\n")
    if startStroka == base:
        startStroka = baseStroka
        print(startStroka)
    firstSplitStroka = startStroka.split(" ")
    count = 0
    for i in firstSplitStroka:
        if i[0] in ABC or (i[0]=="," and i[0] in ABC):
            firstSplitStroka[count] = firstSplitStroka[count].upper()
        count+=1
    endStroka = " ".join(firstSplitStroka)
    print(endStroka)

def Ex6():
    ReadCSV(num=6)
    myDict = dict()
    string = input("Введите символы:\n")
    for i in string:
        myDict[i] = 0
    for i in string:
        myDict[i] = myDict[i]+1
            
    string =""
    for i in myDict:
        if myDict[i] == 1:
            string = string+ i
    print(string)


def Ex7():
    ReadCSV(num=7)
    base = ["www.bibANDbob.ru","borisBAD.com","www.sven.org"]
    http = "http://"
    www = "www."
    com = ".com"
    strings = list()
    for i in base:
        string=""
        if www in i:
            string = http+i
            if com not in i:
                string = string+ com
            strings.append(string)

    res = [http + i for i in base if(www in i)]
    fullres = [i+com if(com not in i)else i for i in res]

    print(strings)
    print(fullres)

    

def Ex8():
    ReadCSV(num=8)
    n = random.randint(0,10000)
    pow = 1
    array = list()
    while n > 0:
        n = n-1
        array.append(random.randint(0,100))   
    if(n<=2):
        for i in range(len(array),2):
            array.append(random.randint(0,100))
    print("Было элементов",len(array))
    while True:
        if 2 ** pow <= len(array) and len(array) <= 2**(pow+1): #между двумя значениями
            print("между ",2**pow," и ",2**(pow+1))
            array = Ex8_1(array,2**(pow+1)-len(array))
            break
        pow = pow+1
    print("Стало элементов",len(array))
    print(array)
    
def Ex8_1(array,add):
    for i in range(1,add+1):
        array.append(random.randint(0,100))
    return array 

base = "base"
basegood ="basegood"
basebad = "basebad"
Ex7()

