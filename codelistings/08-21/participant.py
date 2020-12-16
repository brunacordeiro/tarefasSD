import channel, stablelog, random #-
from const2PC import * #-

class Participant:
  def __init__(self): #-
    self.chan        = channel.Channel() #-
    self.participant = self.chan.join('participant') #-
    self.log         = stablelog.createLog(self.participant) #-
#-
  def do_work(self): #-
    return random.choice([LOCAL_ABORT, LOCAL_SUCCESS]) #-
#-
  def run(self):
    self.chan.bind(self.participant) #-
    coordinator      = self.chan.subgroup('coordinator') #-
    all_participants = self.chan.subgroup('participant') #-
    self.log.info('INIT') 
#-
    msg = self.chan.recvFrom(coordinator, TIMEOUT)
    if (not msg):  # Crashed coordinator - give up entirely
      decision = LOCAL_ABORT
    else: # Coordinator will have sent VOTE_REQUEST
      decision = self.do_work() 
      if decision == LOCAL_ABORT:
        self.chan.sendTo(coordinator, VOTE_ABORT)
#-
      else: # Ready to commit, enter READY state
        self.log.info('READY') 
        self.chan.sendTo(coordinator, VOTE_COMMIT)
#-
        msg = self.chan.recvFrom(coordinator, TIMEOUT)
        if (not msg): # Crashed coordinator - check the others
          self.chan.sendTo(all_participants, NEED_DECISION)
          while True:
            msg = self.chan.recvFromAny()
            if msg[1] in [GLOBAL_COMMIT, GLOBAL_ABORT, LOCAL_ABORT]:
              decision = msg[1]
              break
#-
        else: # Coordinator came to a decision
          decision = msg[1]
#-
    if decision == GLOBAL_COMMIT: 
      self.log.info('COMMIT')
    else: # decision in [GLOBAL_ABORT, LOCAL_ABORT]:
      self.log.info('ABORT')
#-
    while True: # Help any other participant when coordinator crashed
      msg = self.chan.recvFrom(all_participants)
      if msg[1] == NEED_DECISION:
        self.chan.sendTo([msg[0]], decision)
