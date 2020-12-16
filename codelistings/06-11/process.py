import channel #-
import random,time #-
from constCS import * #-
#-
class Process:
#-
  def __init__(self, chan):                   
    self.chan       = chan                   # Create ref to actual channel #-
    self.procID     = self.chan.join('proc') # Find out who you are         #-
    self.allProcs   = []                     # All procs in the proc group  #-
    self.otherProcs = []                     # Needed to multicast to others #-
    self.queue      = []                     # The request queue
    self.clock      = 0                      # The current logical clock

  def cleanupQ(self):                        #- 
    if len(self.queue) > 0:                  #-
      self.queue.sort()                      #- 
      # There should never be old ALLOW messages at the head of the queue   #-
      while self.queue[0][2] == ALLOW:       #-
        del(self.queue[0])                   #-
#-
  def requestToEnter(self):                                         
    self.clock = self.clock + 1                         # Increment clock value
    self.queue.append((self.clock, self.procID, ENTER)) # Append request to q
    self.cleanupQ()                                     # Sort the queue
    self.chan.sendTo(self.otherProcs, (self.clock,self.procID,ENTER)) # Send request

  def allowToEnter(self, requester):
    self.clock = self.clock + 1                         # Increment clock value
    self.chan.sendTo([requester], (self.clock,self.procID,ALLOW)) # Permit other

  def release(self):
    assert self.queue[0][1] == self.procID #-
    tmp = [r for r in self.queue[1:] if r[2] == ENTER]  # Remove all ALLOWs
    self.queue = tmp                                    # and copy to new queue
    self.clock = self.clock + 1                         # Increment clock value
    self.chan.sendTo(self.otherProcs, (self.clock,self.procID,RELEASE)) # Release
    
  def allowedToEnter(self):
    commProcs = set([req[1] for req in self.queue[1:]]) # See who has sent a message
    return (self.queue[0][1] == self.procID and len(self.otherProcs) == len(commProcs))

  def receive(self):
    msg = self.chan.recvFrom(self.otherProcs)[1]        # Pick up any message
    self.clock = max(self.clock, msg[0])                # Adjust clock value...
    self.clock = self.clock + 1                         # ...and increment
    if msg[2] == ENTER:                                
      self.queue.append(msg)                            # Append an ENTER request
      self.allowToEnter(msg[1])                         # and unconditionally allow
    elif msg[2] == ALLOW:                              
      self.queue.append(msg)                            # Append an ALLOW
    elif msg[2] == RELEASE:
      assert self.queue[0][1] == msg[1] and self.queue[0][2] == ENTER #-
      del(self.queue[0])                                # Just remove first message
    self.cleanupQ()                                     # And sort and cleanup
#-      
  def run(self): #-
    self.chan.bind(self.procID) #-
    self.allProcs   = self.chan.subgroup('proc') #-
    self.otherProcs = self.chan.subgroup('proc') #-
    self.otherProcs.remove(self.procID)          #-
    self.allProcs.sort()                         #-
    while True:                                  #- 
      if (self.procID != self.allProcs[-1]) and (self.procID == self.allProcs[0] or random.choice([True,False])): #-
        self.requestToEnter()                    #-
        while not self.allowedToEnter():         #-
          self.receive()                         #-
        print " IN:  ", self.procID.zfill(3),    #-
        time.sleep(random.randint(1,5))          #-
        print "-", self.procID.zfill(3)          #-
        self.release()                           #-
        continue                                 #-
      if random.choice([True,False]):            #-
        self.receive()                           #-
