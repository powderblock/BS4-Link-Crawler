from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

our_url = "https://www.census.gov/programs-surveys/popest.html"

html = urlopen(our_url) # Insert your URL to extract
bsObj = BeautifulSoup(html.read());

i = 0

foo_bar = ""

for link in bsObj.find_all('a', href=True):
    i += 1
    link_end = str(link.get('href'))
    if link_end[0] == "#":
        print(link_end)
        continue

    if link_end[0] == "/":
        big_url = str(our_url) + str(link_end)
        foo_bar += big_url + "steve99"
    else:
        foo_bar += str(link.get('href')) + "steve99"

url_list = foo_bar.split("steve99")

#print(url_list)

with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    for url in url_list:
        #print(url)
        wr.writerow([url])

resultFile.close()
