from bs4 import BeautifulSoup
import urllib2

def get_genres(url):
    genres = []
    wiki = url
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)

    try: #Check to see if URL is valid, i.e. 404 errors
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, err:
       if err.code == 404:
           return
       else:
           raise

    soup = BeautifulSoup(page)
    category = soup.find("td","category")
    if category: #check to see if valid URL has genres
        for link in category:
            genre = link.string
            if genre:
                genres.append(genre)
    else:
        return
    return genres
