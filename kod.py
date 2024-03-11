from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
def parse():
    name = []
    new_name = []
    rate = []
    new_rate = []
    rating = {}
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    profile = UserAgent()
    page = requests.get(url, headers={'User-Agent': profile.random})
    soup = BeautifulSoup(page.text, 'html.parser')
    name = soup.findAll('a', class_='ipc-title-link-wrapper')
    rate = soup.findAll('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating' )
    for film in name:
        if film.find('h3') and not(film.find('svg')):
            new_name.append(film.text)
    for i in range(0, 250):
        rating[new_name[i]] = rate[i].text[:3]
    print(rating)