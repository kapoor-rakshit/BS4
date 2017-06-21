import bs4 as bs

soup=bs.BeautifulSoup(open("sample.html"),"lxml")

linklist=soup.find_all("a")

for link in linklist:
	for parent in link.parents:          # .parents gives all the parents of a tag
		print(parent.name)              

for link in linklist:
	print(link.parent.name)              # .parent gives just the immediate parent



bodytags=soup.body.contents             # .contents gives list af all child tags, includes "\n" too... weird

for tag in bodytags: 
	if tag.name!=None:
		print(tag.name)

