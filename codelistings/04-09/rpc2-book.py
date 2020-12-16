import channel, pickle

class Client: 
  def append(self, data, dbList):
    msglst = (APPEND, data, dbList)          # message payload
    msgsnd = pickle.dumps(msglst)            # wrap call 
    self.chan.sendTo(self.server, msgsnd)    # send request to server 
    msgrcv = self.chan.recvFrom(self.server) # wait for response
    retval = pickle.loads(msgrcv[1])         # unwrap return value
    return retval                            # pass it to caller

class Server:
  def run(self):
    while True:
      msgreq = self.chan.recvFromAny() # wait for any request
      client = msgreq[0]               # see who is the caller 
      msgrpc = pickle.loads(msgreq[1]) # unwrap the call
      if APPEND == msgrpc[0]:          # check what is being requested
        result = self.append(msgrpc[1], msgrpc[2]) # do local call 
        msgres = pickle.dumps(result)              # wrap the result
        self.chan.sendTo([client],msgres)          # send response
      
      
    
