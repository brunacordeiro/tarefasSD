import logging

def createLog(name):
	logger = logging.getLogger(str(name))
	logger.addHandler(logging.FileHandler(str(name)+'.log'))
	logger.setLevel(logging.INFO)
	return logger
