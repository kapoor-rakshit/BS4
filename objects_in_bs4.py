# SOURCE : https://github.com/ishan-nitj/beautiful-soup-practice/blob/master/objects_in_BS.py

#There are four kinds of objects in BS:Tag, NavigableString, BeautifulSoup, and Comment

import bs4 as bs

soup=bs.BeautifulSoup(open("sample.html"),"lxml")

#1)Tag
print(type(soup.a))                         # <class 'bs4.element.Tag'>

# attribute types varies, here it is str   
print(type(soup.a["href"]))                # <class 'str'>
# here it is a list
print(type(soup.a["class"]))               # <class 'list'>


#2)NavigableString
print (type(soup.title.string))               # <class 'bs4.element.NavigableString'>

print(type(soup.title.text))                 # <class 'str'>


#3)Beautiful Soup
print(type(soup))                           #<class 'bs4.BeautifulSoup'>


#4)Comment
print(type(soup.p.b.string))                # <class 'bs4.element.Comment'>
print(type(soup.p.b.text))                  # <class 'str'>