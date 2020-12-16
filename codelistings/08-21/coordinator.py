import channel, stablelog #-
from const2PC import *    #-

class Coordinator:
  def __init__(self): #-
    self.chan        = channel.Channel() #-
    self.coordinator = self.chan.join('coordinator') #-
    self.log         = stablelog.createLog(self.coordinator) #-

  def run(self):
    self.chan.bind(self.coordinator)  #-
    self.log.info('INIT')             #-
    participants = self.chan.subgroup('participant') #-
    yetToReceive = list(participants)
    self.log.info('WAIT')
    self.chan.sendTo(participants, VOTE_REQUEST)
    while len(yetToReceive) > 0:
      msg = self.chan.recvFrom(participants, TIMEOUT)
      if (not msg) or (msg[1] == VOTE_ABORT):
        self.log.info('ABORT')
        self.chan.sendTo(participants, GLOBAL_ABORT)
        return
      else: # msg[1] == VOTE_COMMIT
        yetToReceive.remove(msg[0])
    self.log.info('COMMIT')
    self.chan.sendTo(participants, GLOBAL_COMMIT)
