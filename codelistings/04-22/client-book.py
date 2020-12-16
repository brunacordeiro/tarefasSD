import zmq
context = zmq.Context()

php = "tcp://"+ HOST +":"+ PORT # how and where to connect
s   = context.socket(zmq.REQ)   # create socket

s.connect(php)                  # block until connected
s.send("Hello World")           # send message
message = s.recv()              # block until response
s.send("STOP")                  # tell server to stop
print message                   # print result
