__author__="bhaskar kalia"
__date__="Tue Oct 7"
__description__="Main Interface of the Crawler"

#!/usr/bin/env

from Tkinter import *
import tkMessageBox
from crawler import crawler
import urllib2
import sys
import re
from BeautifulSoup import *
import subprocess

class Application(Frame):
	#self.var=StringVar()
	#self.var.set("Starting Crawling\n")

	def start_crawling(self): #method to start crawling
		seed=self.seed.get("1.0","end-1c")
		#tkMessageBox.showinfo("Title",seed)
		craw=crawler(seed)
		count=0
		message=""

		#crawling algorithm here :) :) 
		while not craw.is_empty() and count<5 : #configure count's value according to your choice
			count=count+1
			url=craw.remove_url()
			if not craw.is_visited(url):
				craw.add_visited(url)
				pattern=re.compile('http://*')
				
				pattern1=re.compile('.*pdf') #ignoring pdf 
				pattern2=re.compile('.*gif')  #ignoring gif
				pattern3=re.compile('.*jpg')  #ignoring jpg
				pattern4=re.compile('.*jpeg') #ignoring jpeg
				pattern5=re.compile('.*link') #ignoring  forwarding error 503 to some extent
				
				matcher=pattern.match(url)
				matcher1=pattern1.match(url)
				matcher2=pattern2.match(url)
				matcher3=pattern3.match(url)
				matcher4=pattern4.match(url)
				matcher5=pattern5.match(url)

				if matcher and not (matcher1 or matcher2 or matcher3 or matcher4 or matcher5):
					print url + "\nThis is a valid url \nGoing to crawl it NOW !"
					
					#start crawling here
					request=urllib2.Request(url)
					response=urllib2.urlopen(request)
					#content=response.decode('utf-8')
					#could handle exception here
					content=response.read()  #getting the content from the current uniform resource locator :) cool stuff
					#parsing the html content to get all the href links from current page
					soup=BeautifulSoup(content) #creating soup of content
					#write code to save this content in some file on the disk 
					filename="/home/bhaskar/Documents/programming/python/pythonGuiTkinter/crawlerProject/crawledFiles/"+soup.title.string+".txt"
					fileObject=open(filename,"wb")
					fileObject.write(soup.prettify())
					print "URL's found in this Page are :"
					#enqueuing all the href links from the current page/resource
					for link in soup.findAll('a'):
						craw.add_url(link.get('href'))
						print link.get('href')
				
				#terminating for testing 
				else:
					#message=message+"\n\n"+url + "\n\nThis is a invalid url \nNot going to crawl it NOW !"
					print url+"\nThis is invalid url\nNot going to crawl it !"	
				
		print "I have reached the end"
		self.show.config(state="normal") #enabling the show downloaded files button

	def show_files(self): #method to show files (downloaded) open downloaded files folder
		subprocess.call("gnome-open /home/bhaskar/Documents/programming/python/pythonGuiTkinter/crawlerProject/crawledFiles",shell=True)

	def createWidgets(self): #method to create the widgets on the main Interface
		
		
		"""
		#lets put the text box here
		self.textBox=Text(self)
		self.textBox["width"]=40
		self.textBox["bg"]="white"
		self.textBox.pack(expand=True,fill='both',side="left")
		"""
		
		
		#creating label for the crawler
		self.label=Label(self,text="Enter Seed")
		self.label.pack()
	
		#creating a textBox for reading the seed value
		self.seed=Text(self)
		self.seed["height"]=1
		self.seed["width"]=60
		self.seed.insert(END,"http://www.google.com")
		self.seed.pack(padx=20)

		#start button here
		self.Start=Button(self)
		self.Start["text"]="Start Crawling"	
		self.Start["fg"]="black"
		self.Start["command"]=self.start_crawling
		self.Start.pack(padx=20,pady=10)
		
		#show downloaded files button button here
		self.show=Button(self)
		self.show["fg"]="black"
		self.show["width"]=21
		self.show["text"]="Show Downloaded Files"
		self.show["command"]=self.show_files
		self.show.config(state="disabled")


		self.show.pack()

		#exit button here
		self.exit=Button(self)
		self.exit["fg"]="red"
		self.exit["text"]="Exit"
		self.exit["command"]=self.quit

		self.exit.pack(padx=20,pady=10)

		"""
		#creating separator line ;)
		separator = Frame(height=2, bd=1, relief=SUNKEN)
		separator.pack(fill=X, padx=5, pady=5)
		"""
		#created by and all details
		self.ref=Label(self)
		self.ref["bg"]="black"
		self.ref["fg"]="white"
		self.ref["text"]="Created By : Bhaskar Kalia\nFinal Year CSE\nRoll Number : 11510\nNIT Hamirpur "
		self.ref.pack(side="bottom")

		

	def __init__(self,master=None):
		self.var=StringVar()
		self.var.set("Starting Crawling\n")
		master.title("Basic Web Crawler")
		# Define frame size and position in the screen :
       		ScreenSizeX = master.winfo_screenwidth()  # Get screen width [pixels]
       		ScreenSizeY = master.winfo_screenheight() # Get screen height [pixels]
       		ScreenRatio = 0.5                              # Set the screen ratio for width and height
       		FrameSizeX  = int(ScreenSizeX * ScreenRatio)
       		FrameSizeY  = int(ScreenSizeY * ScreenRatio)
        	FramePosX   = (ScreenSizeX - FrameSizeX)/2 # Find left and up border of window
      		FramePosY   = (ScreenSizeY - FrameSizeY)/2
		#position frame in the center
      		master.geometry("%sx%s+%s+%s"%(FrameSizeX,300,50,200))

		Frame.__init__(self,master)
		self.pack(padx=20, pady=20)
		self.createWidgets()

root=Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
