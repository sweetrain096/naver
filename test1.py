import sys
import pprint
import requests
from bs4 import BeautifulSoup

sys.stdin = open('movie_urls.txt')

def find_en_title(url):
    req = requests.get(url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    # pprint.pprint(soup)

    tmp_title = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > strong'
    )
    # print(tmp_title)
    # print(tmp_title[0].get('title'))
    en_title = tmp_title[0].get('title')[:-6]
    print(en_title)



def find_genre(url):
    req = requests.get(url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    # pprint.pprint(soup)
    genres = []
    tmp_genres = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a'
    )
    for tmp_genre in tmp_genres:
        genres.append(tmp_genre.text)
        # print(tmp_genre.text)
    print(', '.join(genres))

def find_genre_id(url):
    req = requests.get(url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    # pprint.pprint(soup)
    genres = []
    tmp_genres = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a'
    )
    for tmp_genre in tmp_genres:
        id = int(tmp_genre.get("href").split("=")[1])
        genres.append(id)
    print(genres)
    # f_genre_id.write(str(genres))

def open_date(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tmp_date = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)'
    )
    if tmp_date:
        tmp_date_a = tmp_date[0].select(
            'a'
        )
        open_date_str = ""
        for date in tmp_date_a:
            open_date_str += date.text
        print(open_date_str.split()[-1])
        # f_open_date.write(open_date_str.split()[-1]+"\n")
    else:
        print("")
        # f_open_date.write("\n")

def director(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tmp_director = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a'
    )
    director = tmp_director[0].text
    print(director)
    # f_director.write(director+ '\n')

def actors(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tmp_actors = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p'
    )
    # print(tmp_actors)
    actors = []
    if tmp_actors:
        for actor in tmp_actors[0].select('a'):
            actors.append(actor.text)
        actors = ', '.join(actors)
        print(actors)
    else:
        print(actors)
    # f_actors.write(actors+"\n")

def grade(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tmp_grade = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p'
    )
    # print(tmp_grade)
    if (tmp_grade):
        grade = tmp_grade[0].select('a')

        grade = grade[0].text
        print(grade)
    else:
        grade = ""
        print(grade)
    # f_grade.write(grade + '\n')

def summary(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tmp_summary = soup.select(
        '#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p'
    )
    pprint.pprint(tmp_summary)
    summary = tmp_summary[0]
    print(summary)
    # f_summary.write(summary)
    # f_summary.write("\n")

# f_genre_id = open("./genre_id.txt", 'a')
# f_open_date = open("./open_date.txt", 'a')
# f_director = open("./director.txt", 'a')
# f_actors = open("./actors.txt", "a")
# f_grade = open("./grade.txt", "a")
f_summary = open("./summary.txt", 'a', -1, "utf-8")
for url in sys.stdin:
    try:
        url = str(url[:-1])
        # print(url)
        # find_en_title(url)
        # find_genre(url)
        # find_genre_id(url)
        # open_date(url)
        # director(url)
        # actors(url)
        # grade(url)
        summary(url)

    except StopIteration:
        print("EOF")

# f_genre_id.close()
# f_open_date.close()
# f_director.close()
# f_actors.close()
# f_grade.close()
f_summary.close()

# url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=61823"
#
# url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=151196"
# summary(url)