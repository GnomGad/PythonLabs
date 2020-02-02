import csv
 
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

