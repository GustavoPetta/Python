from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#mostrar no navegafor
driver = webdriver.Chrome("chromedriver.exe")
driver.get(r"https://br.linkedin.com/jobs")

#pra nao ficar abrindo no navegador
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
# driver.get(r"https://br.linkedin.com/jobs")


# login = driver.find_element_by_xpath("""/html/body/nav/section[2]/form/div[1]/div[1]/input""")

# senha = driver.find_element_by_xpath("""/html/body/nav/section[2]/form/div[1]/div[2]/input""")

# button_enter = driver.find_element_by_xpath("""/html/body/nav/section[2]/form/div[2]/button""")
click_pesquisa = driver.find_element_by_xpath("""//*[@id="JOBS"]/section[1]/input""")
click_pesquisa.click()

click_pesquisa.send_keys("Java")

click_out = driver.find_element_by_xpath("""/html/body/main/section[1]/section""")
click_out.click()

# click_location = driver.find_element_by_xpath("""//*[@id="JOBS"]/section[2]/input""")
# click_location.click()


click_button_pesquisa = driver.find_element_by_xpath("""/html/body/main/section[1]/section/div[2]/button[3]""")
click_button_pesquisa.click()
time.sleep(3)

	
	

	
# # page_informations = driver.find_element_by_xpath("""/html/body/main/div/section/ul/li[1]/abrindo""").text
# text = driver.find_element_by_class_name("result-card__full-card-link").getText()
# element = driver.find_element_by_element('//*[@class="job-result-card__snippet"]')

# title = driver.find_element_by_class_name("""result-card__title job-result-card__title""")
# print(title)

# browser = driver.find_element_by_class_name('result-card__full-card-link').click()
# print(browser)


element = driver.find_element_by_css_selector("body")
time.sleep(3)
element.send_keys(Keys.CONTROL+'a')


print("FOI")

print("AAA", element.text)

#time.sleep(10)
#driver.close()