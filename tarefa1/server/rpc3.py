import pickle, os              #-
from socket   import *         #-
from time     import sleep     #-
from random   import *         #-
from constRPC import *         #-
#-
from client   import *         #-
from server   import *         #-
from dbclient import *         #-



pid = os.fork() #-
if pid == 0: #-
  print (f"Iniciando servidor!")
  print (f"IP: {HOST} porta: {PORT}")
  server = Server(PORT) #-
  print (f"Servidor {HOST} iniciado...")
  server.run() #-
  print ("Finalizando servidor...")
  os._exit(0) #-


