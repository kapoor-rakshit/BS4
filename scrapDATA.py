import bs4 as bs
import urllib.request

hindiwebsites = ["https://khabar.ndtv.com/"]
# "https://aajtak.intoday.in/", "https://hindi.moneycontrol.com/"

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
