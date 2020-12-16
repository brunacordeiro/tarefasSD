#!/usr/bin/env python
import os
import channel
import coordinator
import participant

chan = channel.Channel()
chan.channel.flushall()

NP = 3
coord = coordinator.Coordinator()
parts = [participant.Participant() for i in range(NP)]

pid = os.fork()
if pid == 0:
    coord.run()
    os._exit(0)

for i in range(NP):
    pid = os.fork()
    if pid == 0:
        parts[i].run()
        os._exit(0)
