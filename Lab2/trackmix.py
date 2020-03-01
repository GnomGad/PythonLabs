import ffmpeg
import os
import sys
import subprocess


source ="D:\\Application\\Git\\PythonLabs\\Lab2\\TestM"
destination="mix.mp3"
count="-d"
frame="10"
log="-d"
extended="-e"
types = ["trim","concat","fade"]
flag = False


def main():
    musics = os.listdir(source)
    trim(musics)
    concat(musics)
    delet(musics)


def trim(musics):
    for i in musics:
        print(os.path.join(source,i))
        command = "ffmpeg -i \"{0}\" -acodec copy -ss 0 -t \"{2}\"  \"{1}\"".format(os.path.join(source,i),os.path.join(source,types[0]+i),frame)
        subprocess.call(command, shell=True)


def concat(music):
    concats = 0
    subprocess.call("ffmpeg -i \"{0}\" -i \"{1}\" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 {2}".format(os.path.join(source,types[0]+music[0]),os.path.join(source,types[0]+music[1]),os.path.join(source,types[1]+str(0)+".mp3")), shell=True)
    for i in (music):
        if i ==music[0] or i == music[1]:
            continue
        command = "ffmpeg -i \"{0}\" -i \"{1}\" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 {2}".format(os.path.join(source,types[1]+str(concats)+".mp3"),os.path.join(source,types[0]+i),os.path.join(source,types[1]+str(concats+1)+".mp3"))
        subprocess.call(command, shell=True)
        concats+=1
    print(concats)


def delet(musics):
    for i in musics:
        if os.path.isfile(os.path.join(source,types[0]+i)):
            os.remove(os.path.join(source,types[0]+i))
    

    
if __name__ == "__main__":
    for i in range(len(sys.argv)):
        if "--source" == sys.argv[i]:
            source = sys.argv[i+1]
            flag= True
            continue
        if "--destination" == sys.argv[i]:
            destination = sys.argv[i+1]
            continue
        if "--count" == sys.argv[i]:
            count = sys.argv[i+1]
            continue
        if "--frame" == sys.argv[i]:
            frame = sys.argv[i+1]
            continue
        if "--log" == sys.argv[i]:
            log = sys.argv[i+1]
            continue
        if "--extended" == sys.argv[i]:
            extended = sys.argv[i+1]
            continue
    if flag:
        main()