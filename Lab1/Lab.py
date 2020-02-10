
import sys
newpath = sys.path.append(sys.path[0].replace("Lab1",""))
#from MyTools import ReadCSV

import random
import itertools
import math

def Ex1():
    try:
        [print(int(i//1),"рублей",round((i-i//1)*100),"копеек") if i>= 0 else print(0/0) for i in [float(input("Ввод: "))]]
    except ZeroDivisionError:
        print("Некоректный формат")

def Ex2():
    mass = [i for i in input("Введите набор чисел через пробел\n").split(" ")]
    print(False not in [mass[i] < mass[i+1] for i in range(len(mass)-1)])
    
def Ex3():
    snumber = input("Ввод: ").replace(" ","")
    print(snumber.replace(snumber[4:12],'*'*8)) if len(snumber) == 16 else print("Неверно введенный номер")

def Ex4():
    arr = input("Введите текст\n").split(" ")
    [print(i) for i in[print(i) if(i != None and len(i)<7 and len(i)>3 ) else i for i in[print(i) if len(i)>6 else i for i in arr]]if i!=None and len(i)<4]

def Ex5():
    print(" ".join([i.upper() if i[0].isupper() else i for i in input("Ввод:\n").split(" ") ]))
    
def Ex6():
    mass = list(input("Введи текст\n"))
    print("".join([i for i in mass if mass.count(i)==1]))

def Ex7():
    base = ["www.bibANDbob.ru","borisBAD.com","www.sven.org","www.svarm"]
    print(" ".join([i+".com" if(".com" not in i)else i for i in ["http://" + i for i in base if("www." in i)]]))

def Ex8():
    array = [random.randint(0,100) for i in range(0,random.randint(0,10000))]
    print("Было элементов",len(array))
    [array.append(random.randint(0,100)) for i in range(len(array),2**math.ceil(math.log2(len(array))))]
    print("Стало элементов",len(array))
    
def Ex9():
    money = {1000:1,500:10,100:10,50:10,10:1}
    user = int(input("Введите сумму: "))
    if money[1000]*1000+money[500]*500+money[100]*100+money[50]*50+money[10]*10 < user:
        print("В банкомате нет столько денег")
        return 0
    [print("Было ",mul,":",money[mul],"Стало",mul,":",money[mul]-i) for i, mul in Ex9_Generator(money,user)]

def Ex9_Generator(bank,user):
    for i in bank:
        tmp = (user/i)//1 if (user/i)//1 <= bank[i] else bank[i]
        user -= tmp*i
        yield int(tmp), i
        
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
    [print(i) for i in get_frames(range(1,10),4,0.5)]

def get_frames(signal, size=4, overlap=0.5):
    for i in range(0, len(signal) - 1, int(size * overlap)):
        yield [x for x in signal[i : i + size] ]
    
def Ex13():
    [print(elem, cum, frac) for i, elem, cum, frac in extra_enumerate([1,3,4,2])]
    
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
            return  fn([i-a*s[s.index(i)-1] for i in s])
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
#базовые строки
base = "base"
basegood ="basegood"
basebad = "basebad"
#"Константа" в этом модуле не используется
Const_NumExample = 16