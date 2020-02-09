import csv
import Lab1.Lab as lab1
FILENAME = "descriptions.csv"

def WriteCSV(name):
    count = 1
    with open(name, "w", newline="") as file:
        columns = ["#", "Description"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        string = ""
        while True:
            try:
                txt = input()
                if(txt != "qend" and txt != "end"): #qend выход
                    string = string +"\n" +txt
                elif(txt == "end"): #end запись
                    tmp = {"#":count,"Description":string}
                    writer.writerow(tmp)
                    count+=1 
                    string =""
                else:
                    break
            except UnicodeEncodeError as e:
                print("ERROR: ", e)
                string =""
            except:
                print("Error: Что-то новенькое")

def ReadCSV(name=FILENAME, num = 1):
    with open(name, "r", newline="") as file:
        reader = csv.DictReader(file)
        num -=1
        count =0
        for row in reader:
            if count == num:
                print("Номер задания ",row["#"],". ",row["Description"])
                break
            count+=1

def Main(x=0):
    if x == 0:
        [Main(i) for i in range(1,eval(str("lab"+str(1)+".Const_NumExample"))+1)]
        return 0
    print("\n---START Example",x,"---\n")
    strWriteText = "ReadCSV(name=\"Lab"+str(numLab)+"/"+FILENAME+"\",num="+str(x)+")"
    strLaunchEx = "lab"+str(numLab)+".Ex"+str(x)+"()"
    eval(strWriteText)
    eval(strLaunchEx)
    input("\n---TO CONTINUE PRESS ENTER---")

numLab = 1 #Текущая лаба
numEx = 0 # 0 - пройтись по всем 0< выбрать номер
Main(numEx)