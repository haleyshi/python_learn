from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
    print "Root Element: %s" % collection.getAttribute("shelf")

movies = collection.getElementsByTagName("movie")

for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute("title"):
        print "Title:", movie.getAttribute("title")

    type = movie.getElementsByTagName("type")[0]
    print "Type:", type.childNodes[0].data
    format = movie.getElementsByTagName("format")[0]
    print "Format:", format.childNodes[0].data
    #year = movie.getElementsByTagName("year")[0]
    #print "Year:", year.childNodes[0].data
    rating = movie.getElementsByTagName("rating")[0]
    print "Rating:", rating.childNodes[0].data
    stars = movie.getElementsByTagName("stars")[0]
    print "Stars:", stars.childNodes[0].data
    description = movie.getElementsByTagName("description")[0]
    print "Description:", description.childNodes[0].data