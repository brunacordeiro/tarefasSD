import channel, pickle

class DBList:
  def append(self, data):
    self.value = self.value + [data]
    return self

class Client: 
  def append(self, data, dbList):
    msglst = (APPEND, data, dbList)          # message payload
    self.chan.sendTo(self.server, msglst)    # send msg to server 
    msgrcv = self.chan.recvFrom(self.server) # wait for response
    return msgrcv[1]                         # pass it to caller

class Server:
  def append(self, data, dbList):              
    return dbList.append(data)

  def run(self):
    while True:
      msgreq = self.chan.recvFromAny() # wait for any request
      client = msgreq[0]               # see who is the caller 
      msgrpc = msgreq[1]               # fetch call & parameters
      if APPEND == msgrpc[0]:          # check what is being requested
        result = self.append(msgrpc[1], msgrpc[2]) # do local call
        self.chan.sendTo([client],result)          # return response
