from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Users\Jatin Varlyani\Downloads\Compressed\chromedriver_win32\chromedriver.exe')
url = 'https://www.linkedin.com/uas/login'
driver.get(url)

driver.maximize_window()

email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('varlyanijatin08@gmail.com')
time.sleep(1)


password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('password')
time.sleep(1)

login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
login.click()
time.sleep(1)

search = driver.find_element_by_xpath('//*[@id="ember1505"]/input')
search.text('Python Programmers')

#//input[@id='portfolioName'][@type='text']
# search = driver.find_element_by_class_name('ember-view')
# search.send_keys('Python Programmers')

button = driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button/span/li-icon/svg')
button.click()


people = driver.find_element_by_xpath('//*[@id="ember4248"]/ul/li[1]/button')
people.click()


#driver.quit()
