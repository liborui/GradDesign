#-*- coding: UTF-8 -*-
import psutil,time
import sys
import datetime



in_pidMain = int(sys.argv[1])
in_pidFlash = int(sys.argv[2])
in_pidGPU = int(sys.argv[3])
in_time = int(sys.argv[4])
in_tag = sys.argv[5]

timeStamp = datetime.datetime.now().strftime('%m%d_%H%M%S')
cpu_strFile = ".\\flash\\"+timeStamp+in_tag+"cpu"+".txt"
mem_strFile = ".\\flash\\"+timeStamp+in_tag+"mem"+".txt"

f = open(cpu_strFile,"w+")
f_mem = open(mem_strFile,"w+")

i = 0
while i<in_time:
    p1 = psutil.Process(pid=in_pidMain)
    p1.cpu_percent(interval=0)
    p2 = psutil.Process(pid=in_pidFlash)
    p2.cpu_percent(interval=0)
    p3 = psutil.Process(pid=in_pidGPU)
    p3.cpu_percent(interval=0)
    time.sleep(1)
    percent1 = p1.cpu_percent(interval=0)
    percent2 = p2.cpu_percent(interval=0)
    percent3 = p3.cpu_percent(interval=0)
    percents=percent1+percent2+percent3
    i = i+1
    percents = percents/8
    print percents
    mem_stat1 = p1.memory_percent()
    mem_stat2 = p2.memory_percent()
    mem_stat3 = p3.memory_percent()
    mem_stat = mem_stat1 + mem_stat2 + mem_stat3
    print mem_stat
    f.write(str(percents))
    f.write("\n")
    f_mem.write(str(mem_stat))
    f_mem.write("\n")

f.close()
f_mem.close()