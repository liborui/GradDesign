import psutil,time
from sys import argv

f = open("flash.txt","w+")

i = 0
while i<240:
    p1 = psutil.Process(pid=8332)
    p1.cpu_percent(interval=0)
    p2 = psutil.Process(pid=4164)
    p2.cpu_percent(interval=0)
    time.sleep(1)
    percent1 = p1.cpu_percent(interval=0)
    percent2 = p2.cpu_percent(interval=0)
    percents=percent1+percent2
    i = i+1
    percents = percents/8
    print percents
    f.write(str(percents))
    f.write("\n")

f.close()