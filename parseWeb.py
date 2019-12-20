import os, subprocess, time, shutil
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%2050001669%20601321570%20601321572%20601323902%20601328427%20601331000%20601331379%20600419577%20600536666%20601341679&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1"

#opening up connection
uClient = urlopen(my_url)

#collects the content of the html page as raw text
page_html = uClient.read()

uClient.close() #closes connection

#cleans the raw text
pageSoup = soup(page_html, "html.parser")

#print(pageSoup.p) finds first <p> class

containers = pageSoup.findAll("div", {"class":"item-container"})

contain = container[0]
print(containers)

'''
import urllib.request
>>> class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


>>> opener = AppURLopener()

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: AppURLopener style of invoking requests is deprecated. Use newer urlopen functions/methods
>>> webpage = opener.open("https://mangarock.com/manga/mrs-serie-265208/")
'''
