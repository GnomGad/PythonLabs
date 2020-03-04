import os
import hashlib
import random
import re
import subprocess


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


def Ex3():
    path = os.getcwd()+"\\Music"
    getMusic = "E:\\VKMusic 4\\Music"
    if not os.path.exists(path):
        os.mkdir(path)
    Ex3_CreateMusics(os.getcwd())
    Ex3_CreateDurations(os.getcwd())
    Ex3_CreateList(os.getcwd())
    Ex3_Rename(path)


def Ex3_Rename(path):
    for filename in os.listdir(path):
        if filename[-4:] ==".mp3":
            for i in Ex3_GetList(path+"\\Musics.txt"):
                if (filename[:-4]) in i and os.path.exists(path+"\\"+filename):
                    os.replace(path+"\\"+filename,path+"\\"+i[:-1])
                    break


def Ex3_CreateMusics(path):   
    for i in Ex3_GetList(path+"\\MusicNames.txt"):
        with open(path+"\\Music\\"+i[:-1], "w+",encoding="UTF-8") as file:
            pass


def Ex3_CreateDurations(path):
    with open(path+"\\MusicDurations.txt", "w+",encoding="UTF-8") as file:
        for i in Ex3_GetList(path+"\\MusicNames.txt"):
            file.write("[{0}.{1}]\n".format(random.randint(0,9),random.randint(10,60)))


def Ex3_CreateList(path):
    with open(path+"\\Music\\Musics.txt", "w+",encoding="UTF-8") as file:
        mus =Ex3_GetList(path+"\\MusicNames.txt")
        dur =Ex3_GetList(path+"\\MusicDurations.txt")
        for i in range(len(mus)):
            file.write(str(i+1)+". "+mus[i][:-5]+" "+dur[i][:-1]+".mp3\n")


def Ex3_GetList(path):  
    with open(path, "r",encoding="UTF-8") as file:
        return file.readlines()


def Ex4():
    lst = []

    reg = "(:(-)?[\)]+)|\){3,}"
    while True:
        t = input()
        if t == "":
            break
        else:
            lst.append(t)
            
    [print("Строка,",i,"позиция",j,": найдено",res) for i, j, res in TestReg(lst,reg)]
        

def TestReg(lst,reg):
    for i in range(len(lst)):
        parser = re.search(reg,lst[i])
        count =0
        while parser!=None:
            yield i+1,parser.regs[0][0]+count+1,parser.group()
            count+=parser.regs[0][1]
            lst[i] = lst[i][parser.regs[0][1]:]
            parser = re.search(reg,lst[i])
            

def Ex5():
    reg = "[A-ZА-ЯЁ][A-ZА-ЯЁa-zа-яё]+([0-9]{4}$|[0-9]{2}$)"
    [print(res) for i, j, res in TestReg(input().split(),reg)]

    
def Ex6():
    subprocess.call("reorganize.py --source \"D:\\TestDir\" --days 2 --size 4096",shell=True)


def Ex7():
    subprocess.call("trackmix.py -s \"D:\\Application\\Git\\PythonLabs\\Lab2\\TestM\" -d \"kek.mp3\" -f 15 -l --extended",shell=True)


Ex7()   