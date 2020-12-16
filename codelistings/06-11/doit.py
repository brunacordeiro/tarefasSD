import sys,os,time
import channel
import process
from constCS import *

n = 30 # int(sys.argv[2]) # 8
chan = channel.Channel(nBits=7)
chan.channel.flushall()

procs  = [process.Process(chan) for i in range(n)]

for i in range(n):
	pid = os.fork()
	if pid == 0:
		procs[i].run()
		os._exit(0)
	time.sleep(0.25)

os._exit(0)
close(fd)
