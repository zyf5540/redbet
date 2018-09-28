# coding=utf8
import requests
from bs4 import BeautifulSoup
import lxml
url = 'http://live.500.com/2h1.php'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
#soup1 = soup.find_all('tr',{'status':'3'})
id = re.match()
for i in soup:
    #id = i.find_all('td','class':'ssbox_01')
  # 'span', {'class': 'course-per-num', 'class': 'pull-left'}).get_text()
    print (i)
