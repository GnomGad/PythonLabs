import os
import hashlib


def Ex1():
    rus = "йцукенгшщзхъфывапролджэячсмитьбюё"
    eng = "qwertyuiopasdfghjklzxcvbnm"
    Ex1_Result(rus,"Ex1Text.txt")


def Ex1_Result(lang,path):
    with open(path, "r") as file:
        text = file.read().lower()
        dtext = {i:text.count(i) for i in lang}
        [print(i[0],"-",round(i[1]/len(dtext),2),"%") for i in sorted(dtext.items(),key = lambda i: i[1],reverse=True)]
    

def Ex2():
    pass


Ex1()