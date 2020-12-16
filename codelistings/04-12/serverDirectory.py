
import rpyc
from constRPYC import * 
from rpyc.utils.server import ForkingServer

class ServerDirectory(rpyc.Service):
    registryDirectory = {}

    def exposed_register(self, server_name, my_ip_adress, port_number):
    	self.registryDirectory[server_name] = (my_ip_adress, port_number)
    	print (self.registryDirectory)
    
    def exposed_lookup(self, server_name):
        if server_name in self.registryDirectory:
            return self.registryDirectory[server_name]
        else:
            return None

if __name__ == "__main__":
    server_dir = ForkingServer(ServerDirectory, port = '' )
    server_dir.start()
    
