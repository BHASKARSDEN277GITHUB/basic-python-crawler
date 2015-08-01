__author__="bhaskar kalia"
__date__="Tue Oct 7"
__description__="Queue datastructure to store the url's"

#!/usr/bin/env

class queue:
	def __init__(self):
		self.list=[]
	def enqueue(self,item):
		self.list.insert(0,item)
	def dequeue(self):
		return self.list.pop()
	def isEmpty(self):
		return self.list==[]
	def size(self):
		return len(self.list)

