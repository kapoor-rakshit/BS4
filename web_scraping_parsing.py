import bs4 as bs
import urllib.request
# import urllib  : for python2.x  as request is not a module 

site=urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# site=urllib.urlopen("----site to be scraped-------").read()  :  for python2.x  as request is not a module

soup=bs.BeautifulSoup(site,"lxml")     # BeautifulSoup object (page,parser)

"""print(site)"""
"""print(soup.prettify())"""           # entire HTML code, prettify makes it aligned well

print(soup.title)                      # finds the title tag with content : <title>Python Programming Tutorials</title>
print(soup.title.name)                 # name of a tag : title

print(soup.title.string)               # title's content  : Python Programming Tutorials
                                       # .string does not work with tag containing child tags, shows None 
print(soup.title.text)                 # .text works with tags containing child tags also

print(soup.title.parent.name)          # work on parent of a tag , here is <head>

print(soup.find_all(class_="modal"))   # list of data within tags having class="modal"

print(soup.find_all(id="searchform"))  # use soup.find(id="searchform") as id is unique, and class not

paras=soup.find_all("p")               # a list of all specified tag and their contents
for i in paras:
	print(i.text)
print()
print(soup.p)                          # just the first of specified tag

print(soup.get_text())                 # get all the text in website

for i in soup.find_all("a"):           # get all links 
	print(i.get("href"))

print(soup.meta["content"])            # get attribute(content) value of a tag(meta) 
soup.meta["content"]="dummy"
print(soup.meta["content"])            # modified value of attribute

soup.meta["dummyattr"]=1256            # add an attribute

del soup.meta["name"]                  # remove an attribute

print(soup.meta.attrs)                 # dict of attributes as keys and values as values {attribute:value}

