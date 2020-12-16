class DBClient:
  def sendrecv(self, message):
    sock = socket()                        # create a socket
    sock.connect((self.host, self.port))   # connect to server
    sock.send(pickle.dumps(message))       # send some data
    result = pickle.loads(sock.recv(1024)) # receive the response
    sock.close()                           # close the connection
    return result

  def create(self):
    self.listID = self.sendrecv([CREATE])
    return self.listID
  
  def getValue(self):
    return self.sendrecv([GETVALUE, self.listID])
    
  def appendData(self, data):
    return self.sendrecv([APPEND, data, self.listID])
