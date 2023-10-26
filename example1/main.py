import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie

URL =  'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report'


def main():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())


    #document.querySelector("#mw-content-text > div.mw-parser-output > table.wikitable > tbody > tr:nth-child(2) > td:nth-child(2) > a")
    article = soup.select('tr')
    title = soup.select('tr td:nth-child(2) a')
    rank = soup.select('tr td:nth-child(1)')

    # def get_year(movie_tag):
    #     moviesplit = movie_tag.text.split()
    #     year = moviesplit[-1] # last item 
    #     return year

    # years = [get_year(tag) for tag in movietags]
    title_list =[tag['title'] for tag in title][1:] # access attribute 'title'
    # titles = [tag.text for tag in inner_movietags]
    rank_list = [x.text.replace('\n', '') for x in rank][1:]

    n_titles = len(title_list)

    while(True):
        idx = random.randrange(0, n_titles)
        
        print(f'{title_list[idx]}, {rank_list[idx]}')

        # comment the next line out to test user input with docker run -t -i
        # break
    
        user_input = input('Do you want another wiki (y/[n])? ')
        if user_input != 'y':
            break
    

if __name__ == '__main__':
    main()
