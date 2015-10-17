import hashlib
import time


def getDynamicPassword(a):
	# call calculateNormalizedTimeFromBegin and concatenate
	# with input, return sha1 hash
	a = str(calculateNormalizedTimeFromBegin()) + a
	return hashlib.sha1(a.encode('utf8')).hexdigest()

def calculateNormalizedTimeFromBegin():
	# get the UNIX time in seconds, divide by 900
	# round and multiply by 900
	a = time.time() / 900
	return round(a) * 900
