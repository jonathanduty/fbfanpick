import urllib
from  sgmllib import SGMLParser
from lxml import etree

_NFL_URL = "http://sports.espn.go.com/nfl/schedule"


class BaseHTMLProcessor(SGMLParser):
    
    
    def reset(self):                        
        SGMLParser.reset(self)
        

    def start_tr(self,attrs):
           print "starting td"
    def start_td(self,attrs):
        print "starting td"
    
    def handle_data(self, text): 
        print text
    # def unknown_starttag(self, tag, attrs):                 
    #     print "Encountered the beginning of a %s tag" % tag
    # 
    # def unknown_endtag(self, tag):
    #     print "Encountered the end of a %s tag" % tag
        
        
def parse_nfl():

    f = urllib.urlopen(_NFL_URL)
    
    s = f.read()
    document = etree.HTML(s)
    
    tables =  document.xpath('//table')
    for table in tables[1:3]:
        if table.get("class") == "tablehead":
            for row in table:
            
                # figure out if we are looking at a "week 1" row
                if row.get("class") == "stathead":
                    for col in row:
                        print "Week: ",col[0].text
                elif row.get("class") == "colhead":
                    date = row[0].text
                    print "Game Date",date
                
                elif row.get("class") in ["oddrow","evenrow"]:
                    # we are only interested in thei first
                    col = row[0]
                    print "Team A ",col[0].text
                    print "Team b ",col[1].text
                    
    f.close()