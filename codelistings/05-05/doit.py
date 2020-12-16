#!/usr/bin/env python
import sys,os,time
import channel
import chord
from constChord import *

m = int(sys.argv[1]) # 5
n = int(sys.argv[2]) # 8

chan = channel.Channel(nBits=m)
chan.channel.flushall()

nodes  = [chord.ChordNode(chan) for i in range(n)]
client = chord.ChordClient(chan)

for i in range(n):
	pid = os.fork()
	if pid == 0:
		nodes[i].run()
		os._exit(0)
	time.sleep(0.25)

pid = os.fork()
if pid == 0:
	client.run()
	os._exit(0)

os._exit(0)
