import os, subprocess, time, shutil, datetime
import urllib.request
from urllib.request import Request, urlopen
import bs4
from bs4 import BeautifulSoup as soup
import re

def getSoup(website):
    request = Request(website, headers={'User-Agent':'Mozilla/5.0'}) #connects to the website and reads it as coded
    rawPage = urlopen(request).read()#extracts content of website
    codePage = rawPage.decode('utf-8')#decodes the content

    page = soup(codePage, "html.parser")#this will beautify the webpage
    return page

def isOpen(rink):
    rinkName = rink.find("div", {"class": "accbox"}).find(("h1"), recursive=False).get_text().strip()
    table = rink.find("tr", {"id":"dropin_Skating_0"}).find(("tbody"))
    rinkTimes = [] 
    for i in table.findChildren("tr", recursive=True):
    	txt = i.find("span").get_text()
    	if txt == "Shinny: Adult":
    		for k in i.findAll("td"):
    			#print(k)
    			if re.search("am", k.get_text()) or re.search("pm", k.get_text()):#this will get rid of the last comma
    				y = re.sub("am", ", ", k.get_text())# get rid of am
    				x = re.sub("pm", ", ", y)# get rid of pm
    				z = x[:-2]
    			else:
    				z = k.get_text() 


    			if k.get_text() == u'\xa0': #replace those utf blanks
    				rinkTimes.append("")
    			else:
    				rinkTimes.append(z)
    		break

    if datetime.datetime.today().weekday() <= 5:
        weekDay = datetime.datetime.today().weekday()+1
    else:
        weekDay = datetime.datetime.today().weekday()-6
   
    if not rinkTimes or not rinkTimes[weekDay]:#if entry is empty
    	print("{:30} -- {:10}".format(rinkName, "N/A"))
    else:
    	print("{:30} -- {:10}".format(rinkName, rinkTimes[weekDay]))

def start(web):
	x = getSoup(web)
	isOpen(x)

def main():

	print("Adult Shinny Times:")
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/629/index.html")#cedervale
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/260/index.html")#wallace
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/638/index.html")#glenLong
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/196/index.html")#ChristiePits
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/87/index.html")#DufferinGrove
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/251/index.html")#otterCreek
	start("https://www.toronto.ca/data/parks/prd/facilities/complex/1220/index.html")#hodgson

if __name__ == '__main__':
	main()
