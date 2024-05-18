import requests
from bs4 import BeautifulSoup
import pandas as pd 

header = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


req = requests.get("https://www.imdb.com/chart/top/" , headers = header)
soup = BeautifulSoup(req.text,"html.parser")

find_ul = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base')
find_li = find_ul.findAll("li")

tag_a = []
for tag in find_li:
    attr = tag.find("a")
    href = attr["href"]
    tag_a.append(href)

story_line = []
titles = []
for link in tag_a:
    req_new = requests.get(f"https://www.imdb.com{link}",headers=header)
    soup_new = BeautifulSoup(req_new.text,"html.parser")
    story_title = soup_new.find("span",class_='sc-7193fc79-1 jgFQCx')
    find_title = soup_new.find("span",class_="hero__primary-text")
    story_line.append(story_title.text)
    titles.append(find_title.text)






data = pd.DataFrame({"title":[title for title in titles],
                     "summerize_movie":[story for story in story_line]})

file_name = "data_imdb.xlsx"
data.to_excel(file_name,index=False)