import pickle, os              #-
from socket   import *         #-
from time     import sleep     #-
from random   import *         #-
from constRPC import *         #-
#-
from client   import *         #-
from server   import *         #-
from dbclient import *         #-


#- client1
sleep(1) #-
pid = os.fork()
if pid == 0:
    print (f"Criando cliente 1 {HOSTCL1} na porta {CLIENT1}")
    client1   = Client(CLIENT1)               # create client
    
    print (f"Criando a referencia remota para o {HOST} na porta {PORT}")
    dbClient1 = DBClient(HOST,PORT)           # create reference
    
    print (f"Criando uma nova lista")
    dbClient1.create()                        # create new list
    
    print (f"Anexando o Cliente 1 na lista de dados")
    dbClient1.appendData('Client 1')          # append some data

    sleep(2) #-
    print (f"Enviando a lista de dados para o Host: {HOSTCL2} na porta: {CLIENT2}")
    client1.sendTo(HOSTCL2,CLIENT2,dbClient1) # send to other client
    print ("Finalizando Cliente 1...")
    os._exit(0) #-

