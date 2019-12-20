import os, sys, time, pprint
from selenium import webdriver
import bs4
from selenium.webdriver.chrome.options import Options
import pyautogui

dir = os.getcwd()

def autoJob(driver, jobID):

	driver.get(r"https://tesla.avature.net/Careers/Success?jobId="+jobID)
	time.sleep(5)
	
	lgnXpth = r'//*[@id="main"]/div/div/section/div[1]/article/div/form/ul/li[1]/a'
	lgn = driver.find_element_by_xpath(lgnXpth)
	lgn.click()

	emailXpth =r'//*[@id="tpt_loginUsername"]'
	email = driver.find_element_by_xpath(emailXpth)
	email.send_keys('kevinjorgo@gmail.com')

	pasXpth =r'//*[@id="tpt_loginPassword"]'
	pas = driver.find_element_by_xpath(pasXpth)
	pas.send_keys('Dragonrider1')

	logXpth = r'//*[@id="main"]/div/div/div/div[1]/section/div/article/div[2]/form/fieldset/div/div[3]/div/button'
	log = driver.find_element_by_xpath(logXpth)
	log.click()
	time.sleep(2)
	'''
	upldXpth = r'//*[@id="134"]'
	upld = driver.find_element_by_xpath(upldXpth)
	upld.click()

	for i in range(8):
		pyautogui.press('tab')
	pyautogui.press('space')
	pyautogui.press('enter')
	'''
	try:
		driver.find_element_by_xpath(r'//*[@id="3842"]').send_keys(r"C:\Users\kevs_\OneDrive\Documents\KevinJorgoFinalResume.pdf")
	except:
		driver.find_element_by_xpath(r'//*[@id="134"]').send_keys(r"C:\Users\kevs_\OneDrive\Documents\KevinJorgoFinalResume.pdf")
	'''
	nxtXpth = r'//*[@id="3843-next"]'
	nxt = driver.find_element_by_xpath(nxtXpth)
	nxt.click()
	time.sleep(5)
	
	nxt2Xpth = r'//*[@id="139-next"]'
	nxt2 = driver.find_element_by_xpath(nxt2Xpth)
	nxt2.click()
	time.sleep(5)
	'''
	nxt2 = driver.find_element_by_class_name("nextButton")
	nxt2.click()

	nxt3 = driver.find_element_by_class_name("nextButton")
	nxt3.click()
	time.sleep(5)

	try:
		#stuXpth = r'//*[@id="3957"]'
		stu = driver.find_element_by_id("3957")
		stu.click()
		pyautogui.press('down')
		pyautogui.press('enter')
		time.sleep(2)


		stu3Xpth = r'//*[@id="3958"]'
		stu3 = driver.find_element_by_xpath(stu3Xpth)
		stu3.click()
		#pyautogui.press('tab')
		pyautogui.typewrite('may')
		pyautogui.press('tab')
		pyautogui.typewrite('2021')

		stu2Xpth = r'//*[@id="3960"]'
		stu2 = driver.find_element_by_xpath(stu2Xpth)
		stu2.click()
		pyautogui.press('down')
		pyautogui.press('enter')
		pyautogui.press('tab')

		pyautogui.typewrite('As a new engineer in the tech industry I am looking to give new insight on old and outdated practices. With my past knowledge I want to increase efficiency and continuously innovate on projects to assist the company. Using my past school and work experience I have fine tuned both my technical prowess as well my people skills. I believe I would make the perfect candidate and can guarantee that I will contribute my all and some.')
		
		#stu3Xpth = r'//*[@id="3962-next"]'
		stu3 = driver.find_element_by_class_name("nextButton")
		stu3.click()
		
	except:
		pass

	menuXpth = r'//*[@id="249"]'
	menu = driver.find_element_by_xpath(menuXpth)
	menu.click()
	pyautogui.press('down')
	pyautogui.press('enter')

	menu2Xpth = r'//*[@id="437"]'
	menu2 = driver.find_element_by_xpath(menu2Xpth)
	menu2.click()
	pyautogui.press('down')
	pyautogui.press('enter')

	noXpth = r'//*[@id="251_38"]'#'//*[@id="3846_38"]'#
	no = driver.find_element_by_xpath(noXpth)
	no.click()

	yesXpth = r'//*[@id="251_38"]'#'//*[@id="3847_37"]'
	yes = driver.find_element_by_xpath(yesXpth)
	yes.click()

	ackXpth = r'//*[@id="2365"]'#'//*[@id="3851"]'#
	ack = driver.find_element_by_class_name("tsla-legalcopy")
	time.sleep(2)
	ack.click()
	#ack.check()
	pyautogui.typewrite("space")

	lglXpth = r'//*[@id="257"]'#'//*[@id="3852"]'
	lgl = driver.find_element_by_class_name("TextField")

	lgl.click()
	pyautogui.typewrite("Kevin Jorgo")

	nxt4Xpth = r'//*[@id="3853-goto"]'#//*[@id="259-goto"]'
	nxt4 = driver.find_element_by_class_name("gotoButton")
	nxt4.click()

	saveXpth = r'//*[@id="3872-save"]'#//*[@id="436-save"]'
	save = driver.find_element_by_class_name("saveButton")
	save.click()


def main():
	i=0
	job =[]
	
	while i<1:
		x = input("Please enter the job ID:").strip() 

		if x != "start":
			job.append(x)
		else:
			break
	

	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	driver =webdriver.Chrome(executable_path=dir+r'\chromedriver.exe', chrome_options=chrome_options)
	#driver.get(r"https://tesla.avature.net/Careers/Success?jobId="+x)

	#autoJob(driver)
	
	for k in range(0, len(job)):
		autoJob(driver, job[k])
	

if __name__ == '__main__':
	main()