from bs4 import BeautifulSoup
from selenium import webdriver

driver  = webdriver.Chrome(executable_path = r'C:\Users\Jatin Varlyani\Downloads\Compressed\chromedriver_win32\chromedriver.exe')

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'

driver.get(url)

#print driver.page_source

soup = BeautifulSoup(driver.page_source, 'lxml')

table = soup.find('table', class_ ='chart')
#print table

for td in table.find_all('td', class_ = 'titleColumn'):
	print td.text.strip().replace('\n','').replace('      ','')