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
# driver.get(r"https://www.indeed.com.br/jobs?q=desenvolvedor&l=São+Paulo&ts=1568076448614&pts=1567187600617&rq=1&fromage=last&newcount=1072")
driver.get(r"https://www.indeed.com.br/empregos?q=desenvolvedor+servicenow&l=São+Paulo")

all_jobs = []
all_link = []
all_locl = []
all_addr = []
all_desc = []


instance = "dev70252"
user = "admin"
pwd = "Sempere2509@"
headers = {"Content-Type":"application/json","Accept":"application/json"}

url_cat = "https://{}.service-now.com/api/now/table/u_jobscrawler".format(instance)

def extract():
	jobs_page = driver.find_elements_by_xpath("""//*[@class="title"]""")
	jobs = [link.text for link in jobs_page]

	link_page = driver.find_elements_by_xpath("""//*[@class="title"]/a""")
	link = [link.get_attribute("href") for link in link_page]

	# locl_page = driver.find_elements_by_xpath("""//*[@class="sjcl"]""")
	locl_page = driver.find_elements_by_xpath("""//*[@class="sjcl"]/div/span""")
	locl = [link.text for link in locl_page]

	addr_page = driver.find_elements_by_xpath("""//*[@class="sjcl"]/span""")
	addr = [link.text for link in addr_page]

	desc_page = driver.find_elements_by_xpath("""//*[@class="summary"]""")
	desc = [link.text for link in jobs_page]

	# print(link)

	all_jobs.append(jobs)
	all_link.append(link)
	all_locl.append(locl)
	all_addr.append(addr)
	all_desc.append(desc)

	# print(driver.current_url)

	next_page()

def next_page():
	try:
		driver.find_element_by_xpath("""//*[contains(text(), 'Próxima')]""").click()
		time.sleep(1)

		try:
			delay = 3 # seconds
			myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'popover-foreground')))
			driver.find_element_by_xpath("""//*[contains(text(), 'Não, obrigado')]""").click()

			extract()

		except:
			pass

			extract()

	except:
		print('FIM!!!')
		driver.close()

def post_jobs(a, b, c, d, e):
	dt_dead = {
		"u_empresa": c,
		"u_site": b,
		"u_posicao": a,
		"u_descricao": e,
		"u_regiao": d
	}
	response = requests.post(url_cat, auth=(user, pwd), headers=headers, json=dt_dead)

extract()

collect_jobs = []
collect_link = []
collect_locl = []
collect_adds = []
collect_desc = []

for i in all_jobs:
	collect_jobs = collect_jobs + i	

for i in all_link:
	collect_link = collect_link + i	

for i in all_locl:
	collect_locl = collect_locl + i	

for i in all_addr:
	collect_adds = collect_adds + i

for i in all_desc:
	collect_desc = collect_desc + i

for a,b,c,d in zip(collect_jobs, collect_link, collect_locl, collect_adds, collect_desc):
	post_jobs(a, b, c, d, e)

###
# PARA ENTENDER SOBRE A LINHA 13 LEIA: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# E ME EXPLICA, PORQUE EU NÃO ENTENDO, SÓ SEI USAR
###

