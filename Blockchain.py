#@Author MAYANK YADAV
from RC6Encryption import RC6Encryption
from Crypto.Cipher import DES
from hashlib import sha256
from aes import AESCipher
from Block import Block
import texrwrap
import time

'''
Remember block structure :
	(previous_hash, data)
here, data is encrypted using AES
'''

class Blockchain():
	def __init__(self):
		block_0 = self.create_genesis_block()
		self.chain = [block_0]

	def create_genesis_block(self):
		genesis_block = Block('0', '') # previous_hash = '0'; no data
		return genesis_block

	def create_new_block(self, encrypted_text):
		'''
		this method is called for storing new data 
		new data is stored as a new block
		'''
		previous_block = self.chain[-1]
		new_block = Block(previous_block.hash, encrypted_text)
		return new_block
