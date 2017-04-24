    #-*- coding: UTF-8 -*-
import psutil,time
import sys
import datetime

f=open("html.txt","w+")

in_pid = int(sys.argv[1])
in_time = int(sys.argv[2])

timeStamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
strFile = ".\\html\\"+"html"+timeStamp+".txt"
f = open(strFile,"w+")

i = 0
while i<in_time:
    p1 = psutil.Process(pid=in_pid)
    p1.cpu_percent(interval=0)
    time.sleep(1)
    percent1 = p1.cpu_percent(interval=0)
    i = i+1
    percents = percent1/8
    print percents
    f.write(str(percents))
    f.write("\n")

f.close()
