import winsound
import time

beepLength=600
frequencyMax=10
fileName="jdk.exe"

with open(fileName, "rb") as f:
    byte = f.read(1)
    last=0
    while byte != "":
        byte = f.read(1)
        i=ord(byte)
        if(i!=0 and i!=255 and i!=last):
            last=i
            i=i*frequencyMax+37
            winsound.Beep(i,beepLength)

 
