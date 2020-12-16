class Client:
  def __init__(self, port):  
    self.host = 'localhost'                # this machine
    self.port = port                       # port it will listen to
    self.sock = socket()                   # socket for incoming calls
    self.sock.bind((self.host, self.port)) # bind socket to an address
    self.sock.listen(2)                    # max num connections

  def sendTo(self, host, port, data):
    sock = socket()               
    sock.connect((host, port))    # connect to server (blocking call)
    sock.send(pickle.dumps(data)) # send some data
    sock.close()

  def recvAny(self):
    (conn, addr) = self.sock.accept()
    return conn.recv(1024)
