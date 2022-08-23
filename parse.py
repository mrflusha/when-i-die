import bs4,sys
from urllib.request import urlopen
import database

webpage = urlopen('file:///home/mrf/vk_arc/Archive/messages/16379605/messages0.html').read().decode('windows-1251')
soup = bs4.BeautifulSoup(webpage, 'html5lib')
text_arr = list()
for text in soup.findAll('div',{"class":"message"}):
	text_arr.append(text.text)
	
print(text_arr[0])


for i in text_arr:
	database.add_to_table(i)


new = database.get_from_db()

print(new[1])