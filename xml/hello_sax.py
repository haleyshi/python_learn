import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == "movie":
            print "*****Movie*****"
            title = attrs["title"]
            print "Title:", title

    def endElement(self, name):
        if name == "type":
            print "Type:", self.type
        elif name == "format":
            print "Format:", self.format
        elif name == "year":
            print "Year:", self.year
        elif name == "rating":
            print "Rating:", self.rating
        elif name == "stars":
            print "Stars:", self.stars
        elif name == "description":
            print "Description:", self.description
        #else:
        #    print "%s tag not parsed.", name

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content
        #else:
        #    print "%s : %s not parsed!" % (self.CurrentData, content)

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = MovieHandler()
    parser.setContentHandler(handler)

    parser.parse("movies.xml")