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
    path = os.getcwd()
    hashes = {}

    for filename in os.listdir(path):
        if os.path.isfile(filename):
            with open(filename, "rb") as file:
                hashes.setdefault(hashlib.md5(file.read()).digest(),[]).append(filename)

    for  filenames in hashes:   
        if len(hashes[filenames]) > 1:
            print("---Файлы Копии---\n", ", ".join(hashes[filenames]), sep="")


Ex2()   