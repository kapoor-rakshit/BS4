import bs4 as bs
import urllib

site=urllib.urlopen("https://pythonprogramming.net/parsememcparseface").read()

soup=bs.BeautifulSoup(site,"lxml")                 # BeautifulSoup object

navkelinks=soup.nav                                # a sub object created to work on with
for i in navkelinks.find_all("a"):
	print(i.get("href"))                           # get links within this <nav> tag only
print()


bodykelinks=soup.body                              # a sub object
for i in bodykelinks.find_all("a"):
	print(i.get("href"))                           # get links within this <body> tag only
print()


for i in soup.find_all("div",class_="modal"):      # find all <div class="modal"> tag whose class is "modal"                                                          
	for j in i.find_all("a"):                     # i is a sub object
		print(j.get("href"))                      # find all links in this object