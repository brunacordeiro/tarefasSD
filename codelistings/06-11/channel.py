import redis
import random, math
import pickle
import os

class Channel():

	def __init__(self, nBits=5, hostIP='localhost', portNo=6379):
		self.channel   = redis.StrictRedis(host=hostIP, port=portNo, db=0)
		self.osmembers = {}
		self.nBits     = nBits
		self.MAXPROC   = pow(2, nBits)

	def join(self, subgroup):
		members = self.channel.smembers('members')
		newpid = random.choice(list(set([str(i) for i in range(self.MAXPROC)]) - members))
		if len(members) > 0:
			xchan = [[str(newpid), other] for other in members] + [[other, str(newpid)] for other in members]
			for xc in xchan:
				self.channel.rpush('xchan',pickle.dumps(xc))
		self.channel.sadd('members',str(newpid))
		self.channel.sadd(subgroup, str(newpid))
		return str(newpid)

	def leave(self, subgroup):
		ospid = os.getpid()
		pid		= self.osmembers[ospid]
		assert self.channel.sismember('members', str(pid)), ''
		del self.osmembers[ospid]
		self.channel.sdel('members',str(pid))
		members = self.channel.smembers('members')
		if len(members) > 0:
			xchan = [[str(pid), other] for other in members] + [[other, str(pid)] for other in members]
			for xc in xchan:
				self.channel.rpop('xchan',pickle.dumps(xc))
		self.channel.sdel(subgroup, str(pid))
		return 

	def exists(self, pid):
		return self.channel.sismember('members', str(pid))

	def bind(self, pid):
		ospid = os.getpid()
		self.osmembers[ospid] = str(pid)
		# print "Process "+str(ospid)+" ["+pid+"] joined "
		# print self.osmembers

	def subgroup(self, subgroup):
		return list(self.channel.smembers(subgroup))

	def sendTo(self, destinationSet, message):
		caller = self.osmembers[os.getpid()]
		assert self.channel.sismember('members', str(caller)), ''
		for i in destinationSet: 
			assert self.channel.sismember('members', str(i)), ''
			self.channel.rpush([str(caller),str(i)], pickle.dumps(message) )

	def sendToAll(self, message):
		caller = self.osmembers[os.getpid()]
		assert self.channel.sismember('members', str(caller)), ''
		for i in self.channel.smembers('members'): 
			self.channel.rpush([str(caller),str(i)], pickle.dumps(message) )

	def recvFromAny(self, timeout=0):
		caller = self.osmembers[os.getpid()]
		assert self.channel.sismember('members', str(caller)), ''
		members = self.channel.smembers('members')
		xchan = [[str(i),str(caller)] for i in members]
		msg = self.channel.blpop(xchan, timeout)
		if msg:
			return [msg[0].split("'")[1],pickle.loads(msg[1])]

	def recvFrom(self, senderSet, timeout=0):
		caller = self.osmembers[os.getpid()]
		assert self.channel.sismember('members', str(caller)), ''
		for i in senderSet: 
			assert self.channel.sismember('members', str(i)), ''
		xchan = [[str(i),str(caller)] for i in senderSet]
		msg = self.channel.blpop(xchan, timeout)
		if msg:
			return [msg[0].split("'")[1],pickle.loads(msg[1])]



				
				
				
