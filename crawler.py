__author__="bhaskar kalia"
__date__="Tue Oct 7"
__description__="crawler class"

#!/usr/bin/env
from q import queue


class crawler:
	
	def __init__(self,seed):
		self.q=queue()  #to hold the unvisited url's
		self.visited=[] #to hold the visited url's
		self.seed=seed
		self.q.enqueue(seed)

	
	def print_seed(self): #to print the seed for the current instance of the crawler
		print self.seed
	
	def add_url(self,url): #to add the url to the queue
		self.q.enqueue(url)
	
	def add_visited(self,url): #to add the url to the visited list
		self.visited.append(url)

	def remove_url(self): #to remove the url from the unvisited queuee
		url = self.q.dequeue()
		return url
	
	def is_empty(self): #to check if the queue is empty
		return self.q.isEmpty()

	def is_visited(self,url): #to check if the  current url is already visited
		s=set(self.visited)
		return url in s
	
	#def download_file(self): #to download the resource at current url
	
	def show_visited_urls(self): #to show the visited urls
		for url in self.visited :
			print url
		print "\n"
		
	#def show_downloaded_files(): #to show the downloaded files
		
