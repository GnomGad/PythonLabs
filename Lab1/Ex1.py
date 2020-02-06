
import sys
newpath = sys.path.append(sys.path[0].replace("Lab1",""))
from MyTools import ReadCSV

import random
import itertools

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
    base = ["www.bibANDbob.ru","borisBAD.com","www.sven.org","www.sven"]
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

def Ex9():
    money = {1000:1,500:10,100:10,50:10,10:1}
    allMoney = Ex9_DictToMoney(money)
    userMoney = 0
    try:
        print("Банкомат имеет: ",allMoney)
        userMoney = int(input("Какую сумму выхотите обналичить?\n"))
        if userMoney%10 != 0:
            raise Exception("Банкомат не выдает мелочь") #Exception("у нас нет мелких денег")
        print(money)
        Ex9_ToCount(money,userMoney)
    except ValueError:
        print("Вы ввели что-то лишнее")
    except Exception as e:
        print(e)
    
def Ex9_MoneyToDict(x):
    thousand = int(x / 1000)//1
    fivehundred = int((x - 1000*thousand)/500) //1
    hundred = int((x - 1000*thousand - 500*fivehundred)/100)//1
    fifty = int((x - 1000*thousand - 500*fivehundred - 100*hundred)/50)//1
    ten = int((x - 1000*thousand - 500*fivehundred - 100*hundred - 50*fifty)/10)//1
    money = {1000:thousand,500:fivehundred,100:thousand,50:fifty,10:ten}
    return money

def Ex9_DictToMoney(x):
    money = x[1000]*1000 +x[500]*500+x[100]*100+x[50]*50+x[10]*10
    return money

def Ex9_ToCount(xList,xInt):
    if(Ex9_DictToMoney(xList)< xInt):
        print("Нужной суммы нет в наличии")
        return 0
    xList,xInt = Ex9_ForCount(xList,xInt,1000)
    xList,xInt = Ex9_ForCount(xList,xInt,500)
    xList,xInt = Ex9_ForCount(xList,xInt,100)
    xList,xInt = Ex9_ForCount(xList,xInt,50)
    xList,xInt = Ex9_ForCount(xList,xInt,10)
    print(xList)
    print(Ex9_DictToMoney(xList))

def Ex9_ForCount(xBank,xUser,div):
    needed = (xUser/div)//1 # то что требуем от банка
    take = xBank[int(div)] - needed # берем у банка
    realTake = take+needed if take<0 else needed # если - то банк дать не может, а значит считаем сколько может дать, если + то забираем что дает
    xUser = xUser - div*realTake # отдаем юзеру его купюры
    xBank[int(div)] =int( xBank[int(div)]-realTake) # говорим банку сколько у него купюр этого типа
    return xBank,int(xUser) # ретурним
        
def Ex10():
    ABC = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"
    abc  = ABC.lower()
    badPasswords = list()
    with open("Passwords.txt", "r") as file:
        badPasswords = file.readlines()
    password = input("Введите пароль\n ")
    if(len(password)>141):
        print("Пароль прошел проверку")
        return 0
    if len(password) <8:
        print("Пароль не прошел проверку")
        return 0
    if password+"\n" in badPasswords:
        print("Пароль не прошел проверку")
        return 0
    for i in abc:
        if password == i* len(password):
            print("Пароль не прошел проверку")
            return 0
    for i in ABC:
        if password == i* len(password):
            print("Пароль не прошел проверку")
            return 0
    print("Пароль прошел проверку")
      
def Ex11():
    for i in frange(1,0,-0.1):
        print(i)
    pass

def frange(start, stop, step):
    i = start
    flag = True
    if start> stop and step <0:
        flag = False

    while i < stop-step and flag:
        yield round(i,1)
        i += step

    while i > stop-step and not flag:
        yield round(i,1)
        i += step

def Ex12():
    pass

def Ex13():
    x = [1,3,4,2]
    for i, elem, cum, frac in extra_enumerate(x):
        print(elem, cum, frac)
    
def extra_enumerate(x):
    cum=0
    summ = 0
    for i in x:
        summ += i
    for i in range(len(x)):
        cum += x[i]
        yield i,x[i],cum, cum/summ
    
def Ex14():
    print(get_pages())

def non_empty(fn):
    def wrapper():
        return[i for i in fn() if i != '' and i != None]
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

def Ex15():
    plot_signal([i for i in range(10)])
    

def pre_process(a=0.97):
    def decoratour(fn):
        def wrapper(s):
            return  fn([i-a*s[s.index(i)-1] for i in s] )
        return wrapper
    return decoratour

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

def Ex16():
    print("---Комманды участники---")
    Grid = Ex16_Generate16Teams()
    date = {"day":14,"month":9,"year":2020,"wednesday":16,"isplay":1}
    for i in Grid:
        print(i)
    
    #print(Grid)
    Ex16_PrintGrid(Grid,1)
    Ex16_PrintGrid(Grid,2)
    Ex16_PrintGrid(Grid,3)
    Ex16_PrintGrid(Grid,4)
    print("\n")
    Ex16_Game(Grid,date)

def Ex16_Game(Grid,date):
    matches = 1
    daysofmounth={9:30,10:31,11:30,12:31,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31}
    while matches <16:
        date["day"]+=1 # апаем день и творим магию
        if(date["day"] == date["wednesday"]): # если день это среда
            date["wednesday"]+=7 # бафаем на некст среду
            if date["isplay"]:
                print("Матч %i будет %i/%i/%i" % (matches,date["day"], date["month"], date["year"]))
                matches+=1
            date["isplay"] = (date["isplay"]+1)%2 # выставляем возможность играть
        if(date["wednesday"] > daysofmounth[date["month"]]): #если дней стало больше чем надо в этом месяце
            #то мы должны от того, что получилось отнять количество дней в некст месяце
            date["wednesday"] -= daysofmounth[date["month"]] if date["month"]+1 <=12 else daysofmounth[1]
        if date["day"] > daysofmounth[date["month"]]: #день вышел за ренж
            date["day"] = 1
            date["month"]+=1
        if date["month"]>12:
            date["month"] = 1
            date["year"] +=1
        
def Ex16_PrintGrid(grid,itoe):
    print("----Сетка ",itoe,"----")
    for i in grid:
        if grid[i] == itoe:
            print(i) 
    
def Ex16_Generate16Teams():
    wordsA = "УЕАОЯИЫ".lower()
    wordsB = "ЙЦКГШЩЗХФВПРЛДЖЧСМТБ".lower()
    aLen = len(wordsA)
    bLen = len(wordsB)
    xList = dict()
    counts = [4,4,4,4]
    counter = 4
    while len(xList) <16:
        nameLen = random.randint(3,12)
        name = ""
        
        reverse = random.randint(0,1)
        for i in range(nameLen):
            if (i+reverse) % 2 ==0:
                name += wordsA[random.randint(0,aLen-1)]
            else:
                name += wordsB[random.randint(0,bLen-1)]
        name = name[0].upper() + name[1:nameLen]

        while True:
            if counter == 0:
                break
            r = random.randint(0,counter-1)
            if counts[r] > 0:
                xList[name] = r+1
                counts[r]-=1
                break
    return xList

#Сделать 12
base = "base"
basegood ="basegood"
basebad = "basebad"

Ex12()