import rpyc
from constRPYC import * #-
from rpyc.utils.server import ForkingServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

if __name__ == "__main__":
  server = ForkingServer(DBList, port = 12345)
  server.start()


'''
# O Server deve registrar o endereço IP e o número de porta (juntamente com seu nome legível) no servidor de diretório.

import socket  #bliblioteca que permite a comunicação entre cliente e servidor


if __name__ == "__main__":
    
    server = ForkingServer(DBList, port = 12345)
    conn_serverDirectory = rpyc.connect(SERVER, PORT)
    
    my_ip_address = socket.gethostbyname(socket.gethostname())
    conn_serverDirectory.root.exposed_register("DBList", my_ip_address, 12345)
    server.start()

'''
