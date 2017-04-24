#-*- coding: UTF-8 -*-
import psutil,time
import sys
import datetime



in_pidMain = int(sys.argv[1])
in_pidFlash = int(sys.argv[2])
in_time = int(sys.argv[3])

timeStamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
strFile = ".\\flash\\"+"flash"+timeStamp+".txt"
f = open(strFile,"w+")

i = 0
while i<in_time:
    p1 = psutil.Process(pid=in_pidMain)
    p1.cpu_percent(interval=0)
    p2 = psutil.Process(pid=in_pidFlash)
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