import bs4 as bs
import urllib.request

site=urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()

"""A Sitemap is an XML file that lists the URLs for a site. 
It allows webmasters to include additional information about each URL: 
when it was last updated, 
how often it changes, 
and how important it is in relation to other URLs in the site. 
This allows search engines to crawl the site more intelligently.

A sitemap can be found at : 
example.com/sitemap.xml
example.com/robots.txt
Google : site:example.com filetype:xml
Google : filetype:xml site:example.com inurl:sitemap

Search (ctrl+f) for .xml"""

soup=bs.BeautifulSoup(site,"xml")                                  # parser for xml is "xml"

urllist=soup.find_all("url")

for url in urllist:                                                # structure of xml
	for loc in url.find_all("loc"):                                # <loc> tag has the url, but it may not be enclosed in the <url> tag always
		print(loc.text)                                            # but in <sitemap> tag : https://www.washingtonpost.com/news-sitemap-index.xml
	for lastmod in url.find_all("lastmod"):                        # Attention : check the sitemap xml format first
		print(lastmod.text)
	print()

