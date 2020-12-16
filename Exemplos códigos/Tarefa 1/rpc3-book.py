pid = os.fork()
if pid == 0:
  client1   = Client(CLIENT1)               # create client
  dbClient1 = DBClient(HOST,PORT)           # create reference
  dbClient1.create()                        # create new list
  dbClient1.appendData('Client 1')          # append some data
  client1.sendTo(HOSTCL2,CLIENT2,dbClient1) # send to other client

pid = os.fork()
if pid == 0:
  client2   = Client(CLIENT2)               # create a new client
  data      = client2.recvAny()             # block until data is sent
  dbClient2 = pickle.loads(data)            # receive reference
  dbClient2.appendData('Client 2')          # append data to same list
