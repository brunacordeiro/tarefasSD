class Process:
  def __init__(self, chan):                   
    self.queue      = []                     # The request queue
    self.clock      = 0                      # The current logical clock

  def requestToEnter(self):                                         
    self.clock = self.clock + 1                         # Increment clock value
    self.queue.append((self.clock, self.procID, ENTER)) # Append request to q
    self.cleanupQ()                                     # Sort the queue
    self.chan.sendTo(self.otherProcs, (self.clock,self.procID,ENTER)) # Send request

  def allowToEnter(self, requester):
    self.clock = self.clock + 1                         # Increment clock value
    self.chan.sendTo([requester], (self.clock,self.procID,ALLOW)) # Permit other

  def release(self):
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
      del(self.queue[0])                                # Just remove first message
    self.cleanupQ()                                     # And sort and cleanup
