import pickle, os       #-
from socket   import *  #-
from random   import *  #-
from constRPC import *  #-
#-
class Server:
  def __init__(self, port=PORT): 
    self.host = 'localhost'               # this machine                     
    self.port = port                      # the port it will listen to 
    self.sock = socket()                  # socket for incoming calls   
    self.sock.bind((self.host,self.port)) # bind socket to an address    
    self.sock.listen(5)                   # max num of connections      
    self.setOfLists = {}                  # init: no lists to manage     

  def run(self):
    while True: 
      (conn, addr) = self.sock.accept() # accept incoming call
      data = conn.recv(1024)            # fetch data from client 
      request = pickle.loads(data)      # unwrap the request
#-
      if request[0] == CREATE:               # create a list       
        listID = len(self.setOfLists) + 1    # allocate listID
        self.setOfLists[listID] = []         # initialize to empty
        conn.send(pickle.dumps(listID))      # return ID

      elif request[0] == APPEND:             # append request
        listID = request[2]                  # fetch listID
        data   = request[1]                  # fetch data to append
        self.setOfLists[listID].append(data) # append it to the list
        conn.send(pickle.dumps(OK))          # return an OK

      elif request[0] == GETVALUE:           # read request
        listID = request[1]                  # fetch listID
        result = self.setOfLists[listID]     # get the elements
        conn.send(pickle.dumps(result))      # return the list
#-
      elif request[0] == STOP:               # request to stop       #-
        conn.close()                         # close the connection  #-
        break                                                        #-
      conn.close()                      # close the connection       
