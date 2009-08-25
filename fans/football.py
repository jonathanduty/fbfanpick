import urllib
from  sgmllib import SGMLParser
from lxml import etree
import csv
import re

_NFL_URL = "http://sports.espn.go.com/nfl/schedule"

# MON, SEP 21
_DATE_FORMAT = r"^(\w*)\W*(\w*)\W*(\w*)$"
#_DATE_FORMAT = "{day_of_week}, {month} {date}" 
_DATE_PARSER = re.compile(_DATE_FORMAT,re.VERBOSE)

_MONTH_TRANSLATION = {
    "JAN":1,
    "FEB":2,
    "MAR":3,
    "APR":4,
    "MAY":5,
    "JUN":6,
    "JUL":7,
    "AUG":8,
    "SEP":9,
    "OCT":10,
    "NOV":11,
    "DEC":12,
}

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
        
        
def parse_nfl(csv_file):

    writer = csv.writer(open(csv_file,'w'))
    
    leage_name = "2009 NFL"

    f = urllib.urlopen(_NFL_URL)
    
    s = f.read()
    document = etree.HTML(s)
    
    tables =  document.xpath('//table')
    for table in tables[1:3]:
        if table.get("class") == "tablehead":
            record = [leage_name,None,None,None]
            for row in table:
            
                # figure out if we are looking at a "week 1" row
                if row.get("class") == "stathead":
                    for col in row:
                        print "Week: ",col[0].text
                elif row.get("class") == "colhead":
                    date = row[0].text
                    print "Game Date",date
                    date_fields = _DATE_PARSER.search(date).groups() #date.parse(_DATE_FORMAT)
                    print "Parse",date_fields
                    record[1] = "%(year)s-%(month)s-%(day)s" % {"day":date_fields[2],
                                                "month":_MONTH_TRANSLATION[date_fields[1]],
                                                "year":"2009"}
                    print "Date",record[1]
                elif row.get("class") in ["oddrow","evenrow"]:
                    # we are only interested in thei first
                    col = row[0]
                    print "Team A ",col[0].text
                    record[2] = col[0].text
                    print "Team b ",col[1].text
                    record[3] = col[1].text
                    writer.writerow(record)
                    
                    print "Record",record
            
    f.close()