from bs4 import BeautifulSoup
from selenium import webdriver


class Film():
	"""docstring for Film"""
	def __init__(self):
		self.rank = ""
		self.title = ""
		self.year = ""
		self.link = ""
	
def get_film_list():	

	driver  = webdriver.Chrome(executable_path = r'C:\Users\Jatin Varlyani\Downloads\Compressed\chromedriver_win32\chromedriver.exe')

	url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'

	driver.get(url)

	#print driver.page_source

	soup = BeautifulSoup(driver.page_source, 'lxml')

	table = soup.find('table', class_ ='chart')

	film_list = []

	#print table

	for td in table.find_all('td', class_ = 'titleColumn'):
		full_title =  td.text.strip().replace('\n','').replace('      ','')
		print full_title

		rank = full_title.split('.')[0]
		print rank

		title = full_title.split('.')[1].split('(')[0]
		print title

		year = full_title.split('(')[1][:-1]
		print year

		a = td.find('a')
		print a['href']

		print '\n'

		new_film = Film()
		new_film.rank = rank
		new_film.title = title
		new_film.year = year
		new_film.link = a['href']

		film_list.append(new_film)


	driver.quit()


	return film_list


film_list = get_film_list()	

for f in film_list:
	print f.title
	print f.rank
	print f.year
	print f.link
