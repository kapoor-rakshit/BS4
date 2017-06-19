import bs4 as bs
import urllib

site=urllib.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

soup=bs.BeautifulSoup(site,"lxml")    # BeautifulSoup object

"""print(site)"""
"""print(soup)"""

print(soup.title)                      # finds the title tag with content : <title>Python Programming Tutorials</title>
print(soup.title.name)                 # name of a tag : title

print(soup.title.string)               # title's content  : Python Programming Tutorials
                                       # .string does not work with tag containing child tags, shows None 
print(soup.title.text)                 # .text works with tags containing child tags also

paras=soup.find_all("p")               # a list of all specified tag and their contents
for i in paras:
	print(i.text)
print()
print(soup.p)                          # just the first of specified tag

print(soup.get_text())                 # get all the text in website

for i in soup.find_all("a"):           # get all links 
	print(i.get("href"))