from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, csv, numpy as np
import pyautogui as py
import sys
reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.Chrome()



def bloomberg_news():
	driver.get("https://www.bloomberg.com/")
	bloomberg = driver.find_element_by_xpath('//*[@id="content"]/div/div/div')
	bnews=bloomberg.text
	print(bnews)
	f=open('todaysnews.txt', 'a')
	f.write(bnews)
	f.write('\n')
	f.close()

def cnn_news():
	driver.get("https://www.cnn.com/")
	cnn=driver.find_element_by_xpath('//*[@id="homepage1-zone-1"]')
	cnnnews=cnn.text
	print(cnnnews)
	f=open('todaysnews.txt', 'a')
	f.write(cnnnews)
	f.close()

def aljazeera():
	driver.get("http://www.aljazeera.com/")
	aljazeera_headlines=driver.find_element_by_xpath('//*[@id="placeholder1"]/div/div[1]/div/div/div[1]/div/section/div/div/div/div[1]/div')
	aljazeera_news=aljazeera_headlines.text
	time.sleep(6)
	aljazeera_headlines.send_keys(Keys.ESCAPE)
	print(aljazeera_news)
	f=open('todaysnews.txt', 'a')
	f.write(aljazeera_news)
	f.close()

def nytimes():
	driver.get("http://www.nytimes.com/")
	nytimes_headlines=driver.find_element_by_xpath('/html/body')
	nytimes=nytimes_headlines.text
	print(nytimes)
	f=open('todaysnews1.txt', 'a')
	f.write(nytimes)
	f.close()

bloomberg_news()
cnn_news()
nytimes()
# aljazeera()






