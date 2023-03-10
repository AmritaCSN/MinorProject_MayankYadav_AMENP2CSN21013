#@Author MAYANK YADAV
import hashlib
import time

class Block:
	def __init__(self, previous_hash, data):
		# data is in encrypted form
		self.timestamp = time.time()
		self.previous_hash = previous_hash
		self.data = data
		self.proof = 0
		is_valid = False

		while(not is_valid):
			self.hash = self.calculate_hash()
			if(self.hash[:2]=='00'): # this determines the difficulty of block mining.
				is_valid = True
			else:
				self.proof += 1

	def calculate_hash(self):
		block_string = f'{self.timestamp}{self.previous_hash}{self.data}{self.proof}'.encode()
		return hashlib.sha256(block_string).hexdigest()
			
