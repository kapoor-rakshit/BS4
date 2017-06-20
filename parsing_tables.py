import bs4 as bs
import urllib.request

site=urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup=bs.BeautifulSoup(site,"lxml")

tablelist=soup.find_all("table")

for table in tablelist:
	for row in table.find_all("tr"):
		k=[]
		for data in row.find_all("td"):
			k.append(data.text)                      # list of data in each row
		print(k)
