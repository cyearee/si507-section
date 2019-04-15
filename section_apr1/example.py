from bs4 import BeautifulSoup 
import requests

url = "https://www.wunderground.com/history/daily/za/matroosfontein/FACT/date/2018-4-1"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text,features="html.parser")
# let's just see if I can get the table element since that's what I'm interested in
print(soup.find('div',class_='summary-table')) # this is getting me "No Data Recorded"
print(soup.find('table')) # I'm getting None!!! D:
print(soup.prettify())