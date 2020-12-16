from socket  import *
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
s.send('Hello, world')  # send same data
data = s.recv(1024)     # receive the response
print data              # print the result
s.close()               # close the connection
