__author__="bhaskar kalia"
__date__="Tue Oct 7"
__description__="User Manual for Basic Single Threaded web Crawler"

1. Run the mainInterface.py using command : python mainInterface.py (Make sure you are connected to the internet)
2. While using socks , user can use : sudo proxychains python mainInterface.py
3. Configure the mainInterface.py at line Number 45 . Specify the directory to store downloaded/crawled files
4. Configure the directory name at line number 63 in mainInterface.py 
   The line looks like :
   subprocess.call("gnome-open /home/bhaskar/Documents/programming/python/pythonGuiTkinter/crawlerProject/crawledFiles",shell=True)
5. configure the value number of url's to be crawled at line number 28 in mainInterface.py
   The line looks like :
    while not craw.is_empty() and count<5 :  #configure count here

