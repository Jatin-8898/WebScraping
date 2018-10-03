from selenium import webdriver
from bs4 import BeautifulSoup
import requests				#Imp Package for getting the img Content

class Film():
	"""docstring for Film"""
	def __init__(self):
		self.rank = ""
		self.title = ""
		self.year = ""
		self.link = ""
	
def get_poster_list():	

	driver  = webdriver.Chrome(executable_path = r'C:\Users\Jatin Varlyani\Downloads\Compressed\chromedriver_win32\chromedriver.exe')

	url = 'https://www.imdb.com/gallery/rg784964352'		#url

	driver.get(url)

	#print driver.page_source

	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_ ='media_index_thumb_list')	#Find the Class

	poster_list = []	#Initialse blank array
	#print div

	for a in div.find_all('a'):
		print a['href']
		print a['title']

		print '\n'

		new_film = Film()
		new_film.title = a['title']
		new_film.link = a['href']

		poster_list.append(new_film)


	driver.quit()

	return poster_list


def downlaod_all_posters(poster_list):

	driver  = webdriver.Chrome(executable_path = r'C:\Users\Jatin Varlyani\Downloads\Compressed\chromedriver_win32\chromedriver.exe')

	for film in poster_list:

		url = 'https://www.imdb.com' + film.link

		driver.get(url)

		soup = BeautifulSoup(driver.page_source,'lxml')

		all_div = soup.find_all('div',class_='pswp__zoom-wrap')

		all_img = all_div[1].find_all('img') 

		print all_img[1]['src']

		f = open('{0}.jpg'.format(film.title.encode('utf8').replace(':','')), 'wb')
		f.write(requests.get(all_img[1]['src']).content)
		f.close()

	driver.quit()

downlaod_all_posters(get_poster_list())
