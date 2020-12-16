import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  conn.root.exposed_append(2)       # Call an exposed operation,
  conn.root.exposed_append(4)       # and append two elements
  print conn.root.exposed_value()   # Print the result
  
  
  
'''
# O cliente usa o nome legível do servidor para descobrir o endereço IP e o número de porta do servidor por meio de uma chamada remota (lookup, via RPC) ao servidor de diretório. 

# Em seguida, o cliente faz uma sequência de chamadas (RPCs) para demonstrar o acesso ao servidor.


  class Client:
    conn_serverDirectory = rpyc.connect(SERVER, PORT)
    nameServerDirectory = conn_directory.root.exposed_lookup("DBList")
  ...  
  
'''

