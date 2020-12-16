import channel, pickle
from constRPC import * #-
                                                #-
class DBList:                                   #-
  def __init__(self, basicList):                #-
    self.value = list(basicList)                #-
                                                #-
  def append(self, data):                       #-
    self.value = self.value + [data]            #-
    return self                                 #-

class Client: 
  def __init__(self):                           #-
    self.chan   = channel.Channel()             #-
    self.client = self.chan.join('client')      #-
                                                #-       
  def run(self):                                #-
    self.chan.bind(self.client)                 #-
    self.server = self.chan.subgroup('server')  #-
                                                #-
  def append(self, data, dbList):
    assert isinstance(dbList, DBList)        #-
    msglst = (APPEND, data, dbList)          # message payload
    msgsnd = pickle.dumps(msglst)            # wrap call 
    self.chan.sendTo(self.server, msgsnd)    # send request to server 
    msgrcv = self.chan.recvFrom(self.server) # wait for response
    retval = pickle.loads(msgrcv[1])         # unwrap return value
    return retval                            # pass it to caller

class Server:
  def __init__(self):                           #-
    self.chan   = channel.Channel()             #-
    self.server = self.chan.join('server')      #-
                                                #-
  def append(self, data, dbList):     #-         
    assert isinstance(dbList, DBList) #- Make sure we have a list
    return dbList.append(data)        #-
                                      #-
  def run(self):
    self.chan.bind(self.server)        #-
    while True:
      msgreq = self.chan.recvFromAny() # wait for any request
      client = msgreq[0]               # see who is the caller 
      msgrpc = pickle.loads(msgreq[1]) # unwrap the call
      if APPEND == msgrpc[0]:          # check what is being requested
        result = self.append(msgrpc[1], msgrpc[2]) # do local call 
        msgres = pickle.dumps(result)              # wrap the result
        self.chan.sendTo([client],msgres)          # send response
      else:                                        #-
        pass # unsupported request, simply ignore  #-
      
      
    
