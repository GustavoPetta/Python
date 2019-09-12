from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import requests, time
from random import *


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)

def acess_site(url):
	driver.get(url)
	extract()

def extract():
	vagas = driver.find_elements_by_xpath("""//*[@class="title"]""")
	vagas = [link.text for link in vagas]
	print(driver.current_url)
	next_page()

def next_page():
	if(driver.find_element_by_xpath("""//*[contains(text(), 'Próxima')]""")):
		driver.find_element_by_xpath("""//*[contains(text(), 'Próxima')]""").click()

		delay = 3 # seconds
		try:
			myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'popover-foreground')))
			driver.find_element_by_xpath("""//*[contains(text(), 'Não, obrigado')]""").click()
			pass
		except TimeoutException:
			pass

		extract()
	else:
		time.sleep(5)
		driver.close()

url = "https://www.indeed.com.br/jobs?q=desenvolvedor&l=São+Paulo&ts=1568076448614&pts=1567187600617&rq=1&fromage=last&newcount=1072"
acess_site(url)

###
# PARA ENTENDER SOBRE A LINHA 13 LEIA: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# E ME EXPLICA, PORQUE EU NÃO ENTENDO, SÓ SEI USAR
###

