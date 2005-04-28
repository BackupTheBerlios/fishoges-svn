

import urllib, htmllib, formatter
format = formatter.NullFormatter()       # create default formatter *
htmlparser = htmllib.HTMLParser(format)  # create new parser object

data = urllib.urlopen("http://www.aquabase.org/fish/dump.php3")
htmlparser.feed(data.read())
htmlparser.close()




class LinksExtractor(htmlparser) # derive new HTML parser

   def __init__(self, formatter) :        # class constructor
      htmllib.HTMLParser.__init__(self, formatter)  # base class constructor
      self.links = []        # create an empty list for storing hyperlinks

   def start_a(self, attrs) :  # override handler of <A ...>...</A> tags
      # process the attributes
      if len(attrs) > 0 :
         for attr in attrs :
            if attr[0] = "href" :         # ignore all non HREF attributes
                self.links.append(attr[1]) # save the link info in the list

    def get_links(self) :     # return the list of extracted links
        return self.links

#Here is the new version of parsing "http://cis.poly.edu/index.htm" 
#using our derived parser:


format = formatter.NullFormatter()           # create default formatter
htmlparser = LinksExtractor(format)        # create new parser object

data = urllib.urlopen("http://www.aquabase.org/fish/dump.php3")
htmlparser.feed(data.read())      # parse the file saving the info about links
htmlparser.close()

links = htmlparser.get_links()   # get the hyperlinks list
print links   # print all the links

#For the crawler assignment we also have to override the start_frame() 
#method to extract the urls of the frames defined in HTML file.




