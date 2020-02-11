
import sys
newpath = sys.path.append(sys.path[0].replace("Lab1",""))
#from MyTools import ReadCSV

import random
import itertools
import math
import re
import datetime

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
    print(snumber[:4] + "*"*8 + snumber[-4:]) if len(snumber) == 16 else print("Неверно введенный номер")

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
    [print(i) for i in frange(0,1,0.1)]

def frange(start, stop, step):
    i = start
    if start > stop and step <0:
        start,stop = stop,start
    while (step>0 and i < stop)or(step <0 and i<=stop and i>start):
        yield i
        i = round(i + step,1)
        
def Ex12():
    [print(i) for i in get_frames(range(1,10),4,0.5)]

def get_frames(signal, size=4, overlap=0.5):
    for i in range(0, len(signal) - 1, int(size * overlap)):
        yield [x for x in signal[i : i + size] ]
    
def Ex13():
    [print(elem, cum, frac) for i, elem, cum, frac in extra_enumerate([1,3,4,2])]
    
def extra_enumerate(x):
    summ,cum = list(itertools.accumulate(x))[-1],0
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
    [print(sample) for sample in s]


def Ex16():
    now = datetime.datetime.now()
    start = datetime.datetime(now.year,9,14,22,45)
    teams = ["Англия","Португалия","Аргентина","Россия","Италия","Китай","Казахстан","Польша","Германия","Франция","Мадагаскар","Афганистан","Украина","Эстония","Канада","Тунис"]
    random.shuffle(teams)
    teams = [teams[i*4:i*4+4] for i in range(0,4)]
    groups = [i for i in itertools.combinations(teams, 4)]
    [print("Группа №",i+1,groups[0][i]) for i in range(0,4)]
    for i in range(1,16):
        print ("Игра #",i,start.strftime("%d/%m/%Y %H:%M"))
        start+=datetime.timedelta(days=14)

Const_NumExample = 16 #"Константа" 

if  __name__ == "__main__":
    pass