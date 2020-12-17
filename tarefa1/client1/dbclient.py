import pickle, os      #-
from socket   import * #-
from constRPC import * #-
#-
class DBClient:
  def __init__(self, host, port, listID=None):  #-
    self.host   = host     # address of server hosting lists        #-
    self.port   = port     # the port it will be listening to       #-
    self.listID = listID   # the list for which this stub is meant  #-
#-
  def sendrecv(self, message):
    sock = socket()                        # create a socket
    sock.connect((self.host, self.port))   # connect to server
    sock.send(pickle.dumps(message))       # send some data
    result = pickle.loads(sock.recv(1024)) # receive the response
    sock.close()                           # close the connection
    return result

  def create(self):
    assert self.listID == None #-
    self.listID = self.sendrecv([CREATE])
    return self.listID
  
  def getValue(self):
    assert self.listID != None #-
    return self.sendrecv([GETVALUE, self.listID])
    
  def appendData(self, data):
    assert self.listID != None #-
    return self.sendrecv([APPEND, data, self.listID])
