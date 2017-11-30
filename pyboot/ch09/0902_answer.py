import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://www.gilbut.co.kr/company/main.aspx')
soup = BeautifulSoup(req,"html.parser")
side_menu = soup.find('div',id='sideNav')
for a_tags in side_menu.find_all('a'):
    print(a_tags['title'])
