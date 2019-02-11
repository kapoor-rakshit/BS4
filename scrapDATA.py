import bs4 as bs
import urllib.request

hindiwebsites = ["https://khabar.ndtv.com/"]

# HINDI SITES
# "https://khabar.ndtv.com/", "https://aajtak.intoday.in/", "https://hindi.moneycontrol.com/",
# "http://hindispot.com", "https://hindividya.com", "http://www.motivationalstoriesinhindi.in",
# "https://yourstory.com/hindi", "http://www.hinditechy.com/", "https://www.gyanipandit.com/", "https://www.onlymyhealth.com/hindi.html",
# "http://hindi.webdunia.com/", "https://www.achhikhabar.com/", "http://nuktachini.debashish.com/", "https://www.hindimehelp.com/",
# "https://www.inditales.com/hindi/", "http://desitraveler.com/flight-to-remember-hindi-blog-post/", "https://www.bharatdarshan.co.nz/literature-collection/2/51/hindi-story.html"

# ENGLISH SITES
# NEWS : https://www.cnbctv18.com/ , https://economictimes.indiatimes.com/ , https://www.livemint.com/ , https://www.bloomberg.com/asia , https://in.mashable.com/
# PROGRAMMING : https://www.geeksforgeeks.org/
# BLOGS : https://www.thefashionspot.com/ , https://abrokenbackpack.com/ , http://theblogabroad.com/
# STORIES : https://www.advance-africa.com/English-Moral-Stories.html
# EDUCATION : http://www.nitj.ac.in/  , http://online.gndu.ac.in/
# COOKING : https://www.vegrecipesofindia.com/ , https://www.rakskitchen.net/ , http://www.manjulaskitchen.com/ , https://www.tastyappetite.net/2013/05/biryani-recipes-biryani-recipe.html , https://www.yummytummyaarthi.com/ , https://www.veganricha.com/ , https://www.ruchiskitchen.com/
# HEALTH : https://www.nih.gov/ , https://www.webmd.com/ , https://www.mayoclinic.org/

hindiwebsitesAtags = []

fileptr = open("data.txt","w+",encoding='utf-8')

for s in hindiwebsites:
	site=urllib.request.urlopen(s).read()

	soup=bs.BeautifulSoup(site,"html.parser")

	atags = soup.find_all("a")
	hrefvals = []
	for i in atags:
		hrefvals.append(i.get("href"))

	hindiwebsitesAtags.extend(hrefvals)

# print(hindiwebsitesAtags)

ignorechars = ['#', '&', '@', '$', '_', '%', '|', "'", ';', ':', '+', '*', '/', '=', '[', ']', '{', '}', '(', ')']
# '-' not added above as in occurrence of 1 - 2

for i in hindiwebsitesAtags:
	try:
		site = urllib.request.urlopen(i).read()
		soup = bs.BeautifulSoup(site, "html.parser")

		ptags = soup.find_all("p")

		for p in ptags:
			tempstr = list(p.text)
			l = len(tempstr)
			for c in range(l):
				if (ord(tempstr[c])>=97 and ord(tempstr[c])<=122) or (ord(tempstr[c])>=65 and ord(tempstr[c])<=90) or (tempstr[c] in ignorechars):
					tempstr[c] = ""
				elif c+1<l and (tempstr[c]=='.' or tempstr[c]=='।') and tempstr[c+1]==' ':
					tempstr[c]='\n'
					tempstr[c+1]='\n'

			tempstr = "".join(tempstr)
			l = len(tempstr)
			flg = 0
			for c in range(l):
				if ord(tempstr[c])>=2304 and ord(tempstr[c])<=2431:
					flg=1
					break

			if flg==1:
				fileptr.write(tempstr)
				fileptr.write("\n\n")

	except Exception as e:
		print(e)

fileptr.close()
