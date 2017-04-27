    #-*- coding: UTF-8 -*-
import psutil,time
import sys
import datetime

in_pid = int(sys.argv[1])
in_time = int(sys.argv[2])
in_tag = sys.argv[3]

timeStamp = datetime.datetime.now().strftime('%m%d_%H%M%S')
cpu_strFile = ".\\html\\"+timeStamp+in_tag+"cpu"+".txt"
mem_strFile = ".\\html\\"+timeStamp+in_tag+"mem"+".txt"

f = open(cpu_strFile,"w+")
f_mem = open(mem_strFile,"w+")

i = 0
while i<in_time:
    p1 = psutil.Process(pid=in_pid)
    p1.cpu_percent(interval=0)
    time.sleep(1)
    percent1 = p1.cpu_percent(interval=0)
    i = i+1
    percents = percent1/8
    print percents
    mem_stat = p1.memory_percent()
    print mem_stat
    f.write(str(percents))
    f.write("\n")
    f_mem.write(str(mem_stat))
    f_mem.write("\n")

f.close()
f_mem.close()