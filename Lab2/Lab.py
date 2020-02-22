import os

def Ex1():
    rus = "йцукенгшщзхъфывапролджэячсмитьбюё"
    eng = "qwertyuiopasdfghjklzxcvbnm"
    with open("Ex1Text.txt", "r") as file:
        text = file.read().lower()
        drus = {i:text.count(i) for i in rus}
        deng = {i:text.count(i) for i in eng}
        print("---РУССКИЙ---")
        dp = list(drus.items())
        dp.sort(key=lambda i: i[1], reverse=True)
        [print(i[0],"-",round(i[1]/len(drus),2),"%") for i in dp]
        print("---ENGLISH---")
        dp = list(deng.items())
        dp.sort(key=lambda i: i[1], reverse=True)
        [print(i[0],"-",round(i[1]/len(deng),2),"%") for i in dp]




Ex1()