import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://www.gilbut.co.kr/company/main.aspx')
soup = BeautifulSoup(req,"html.parser")
contact = soup.find('li',class_='tit3_cont').strong
print(contact.string)
