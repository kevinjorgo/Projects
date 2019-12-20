import os, subprocess, time, shutil
import urllib.request
from urllib.request import Request, urlopen
import bs4
from bs4 import BeautifulSoup as soup
import re

uqHolderWeb = "https://mangarock.com/manga/mrs-serie-265208/"
OnePunchManWeb = "https://mangarock.com/manga/mrs-serie-358279/"
SeraphWeb = "https://mangarock.com/manga/mrs-serie-219943"
BlackCloverWeb = "https://mangarock.com/manga/mrs-serie-28856"
BorutoWeb = "https://mangarock.com/manga/mrs-serie-35593"
NeverlandWeb = "https://mangarock.com/manga/mrs-serie-303939"
SevenWeb = "https://mangarock.com/manga/mrs-serie-172761"
DemonSlayerWeb = "https://mangarock.com/manga/mrs-serie-132938"
AOTWeb = "https://mangarock.com/manga/mrs-serie-295440/"
FFWeb = "https://mangarock.com/manga/mrs-serie-68010"

def getSoup(website):
    request = Request(website, headers={'User-Agent':'Mozilla/5.0'}) #connects to the website and reads it as coded
    rawPage = urlopen(request).read()#extracts content of website
    codePage = rawPage.decode('utf-8')#decodes the content

    page = soup(codePage, "html.parser")#this will beautify the webpage
    return page

def getFinal(manga):
    mangaName = manga.find(class_='_13gHt').get_text()
    mangaFinalCh = manga.find(class_='_1A2Dc rZ05K').get_text()
    mangaDate = manga.find(class_='_2v_aG').get_text()

    #prints it with formatting
    #orderDate(mangaName, mangaDate, mangaFinalCh)
    print("{:40} - {:20} - {:10}".format(mangaName, mangaDate, mangaFinalCh))

def orderDate(name, date, finalCh):
    print("H")
    
def main():

    UQ = getSoup(uqHolderWeb)
    OPM = getSoup(OnePunchManWeb)
    Seraph = getSoup(SeraphWeb)
    BC = getSoup(BlackCloverWeb)
    Boruto = getSoup(BorutoWeb)
    Nvrland = getSoup(NeverlandWeb)
    Seven = getSoup(SevenWeb)
    DmnSlayer = getSoup(DemonSlayerWeb)
    AOT = getSoup(AOTWeb)
    FF = getSoup(FFWeb)

    try:
        getFinal(UQ)
    except Exception :
        pass
    try:
        getFinal(OPM)
    except Exception :
        pass
    try:
        getFinal(Seraph)
    except Exception :
        pass
    try:
        getFinal(BC)
    except Exception :
        pass
    try:
        getFinal(Boruto)
    except Exception :
        pass
    try:
        getFinal(Nvrland)
    except Exception :
        pass
    try:
        getFinal(Seven)
    except Exception :
        pass
    try:
        getFinal(DmnSlayer)
    except Exception :
        pass
    try:
        getFinal(AOT)
    except Exception :
        pass
    try:
        getFinal(FF)
    except Exception :
        pass
    '''
    getFinal(UQ)
    getFinal(OPM)
    getFinal(Seraph)
    getFinal(BC)
    getFinal(Boruto)
    getFinal(Nvrland)
    getFinal(Seven)
    getFinal(DmnSlayer)
    getFinal(AOT)
    getFinal(FF)
    '''
if __name__ == '__main__':
    main()
