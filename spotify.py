import os, sys, time, pprint
from selenium import webdriver
import bs4
from selenium.webdriver.chrome.options import Options
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


dir = os.getcwd()

def dwnldSong(song, driver):
	# options = webdriver.ChromeOptions() 
	# options.add_argument("download.default_directory="+dir)


	txtBarXpath = r'//*[@id="input"]'
	txtBar = driver.find_element_by_xpath(txtBarXpath)
	txtBar.send_keys(song)
	txtBar.submit()

	dwnldXpath = r'/html/body/div[2]/div[1]/div[1]/div[3]/a[1]'
	dwnld =driver.find_element_by_xpath(dwnldXpath)
	driver.implicitly_wait(5)
	dwnld.click()
	time.sleep(20)

	driver.switch_to.window(driver.window_handles[0])

	cnvrtNxtXpath = r'//*[@id="buttons"]/a[3]'
	cnvrtNxt = driver.find_element_by_xpath(cnvrtNxtXpath)
	cnvrtNxt.click()
	time.sleep(5)

def movePlaylist():
	#User id:kevinjorgo?si=5-layoPMQ-iqpOOzAzd9gA
	#prompt for permission
	username = "kevinjorgo"
	

	if len(sys.argv) > 1:
	    search_str = sys.argv[1]
	else:
	    search_str = 'Radiohead'
	    
	client_id = "acf9edccf64c4d56adc29a1843c25d62"
	client_secret = " f2997eabdf7c4ef4b26ee709987a33e4"

	client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	result = sp.search(search_str)
	pprint.pprint(result)

def main():
	i=0
	song = []

	while i<1:
		x = input("Please enter the url's of the songs you want to download and enter 'start' to begin: ").strip() 

		if x != "start":
			song.append(x)
		else:
			break


	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	driver =webdriver.Chrome(executable_path=dir+r'\chromedriver.exe', chrome_options=chrome_options)
	driver.get(r"https://ytmp3.cc/")

	for k in range(0, len(song)):
		dwnldSong(song[k], driver)

if __name__ == '__main__':
	#movePlaylist()
	main()