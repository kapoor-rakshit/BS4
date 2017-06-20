"""SOURCE : https://pythonprogramming.net/javascript-dynamic-scraping-parsing-beautiful-soup-tutorial/
          : https://github.com/niklasb/dryscrape"""

"""websites will supply data that is dynamically loaded via javascript.
   So if we scrape data as normal bs scraping, the script is not rendered and we get default text

    Beautiful Soup doesn't mimic a client. Javascript is code that runs on the client. 
    With Python, we simply make a request to the server, and get the server's response, 
    which is the starting text, along of course with the javascript, 
    but it's the browser that reads and runs that javascript. Thus, we need to do that, mimic as a browser."""

"""dryscrape is a lightweight web scraping library for Python. 
   It uses a headless Webkit instance to evaluate Javascript on the visited pages. 
   This enables painless scraping of plain web pages as well as Javascript heavy Web 2.0 applications like Facebook."""

import dryscrape
import bs4 as bs

sess = dryscrape.Session()
sess.visit('https://pythonprogramming.net/parsememcparseface/')
source = sess.body()

soup = bs.BeautifulSoup(source,'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)                         
                                            
                                            # without dryscrape : y u bad tho?
                                            # with    dryscrape : Look at you shinin!   

            #<script>document.getElementById("txt").innerHTML="Look at you shinin!"</script>