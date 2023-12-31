import requests
from bs4 import BeautifulSoup

from melon_crawling import get_id

url = "https://www.melon.com/chart/index.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
result_chart = soup.find_all(class_=["lst50", "lst100"])  # ==> soup.select(".lst50", ".lst100") 둘은 같은 동작
singer_url = "https://www.melon.com/artist/timeline.htm?artistId="
album_url = "https://www.melon.com/album/detail.htm?albumId="
rank = 1
for i in result_chart:
    song_title = i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".ellipsis.rank02 a")
    singer_id = get_id(singer["href"])
    album = i.select_one(".ellipsis.rank03 a")
    album_id = get_id(album["href"])
    print('%02d' % rank, end="위 \n 제목: ")
    print(song_title, end="\n 가수: ")
    print(singer.text, end="\n 가수 정보 링크: ")
    print(f"{singer_url + singer_id}", end="\n 앨범: ")
    print(album.text, end="\n 앨범 정보 링크: ")
    print(f"{album_url + album_id}")
    rank += 1
    

