import psutil,time
import sys

f = open("flash.txt","w+")

in_pidMain = int(sys.argv[1])
in_pidFlash = int(sys.argv[2])
in_time = int(sys.argv[3])

i = 0
while i<240:
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