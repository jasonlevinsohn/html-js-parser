# NOTES:
# Well this is a good start for replacing text in a file.
# The problem I think is that we are using the HTML Parser.
# So in handle starttag when I ask where the cursor is.  It's at
# the end already because HTML Parser probably parses the whole file
# first.

import fileinput
from HTMLParser import HTMLParser
import sys, re

class myHParser(HTMLParser):
    tempTag = None
    quick_help_array = []
        

    def handle_starttag(self, tag, attrs):
        
        tempTag = self;
        for a in attrs:
            if a[0] == 'data-quickhelp':
                print "Quick Help item found"
                print "    attr: ", a
                self.quick_help_array.append(a[1])
                curPos = f.tell()
                print "Current Position of Cursor: ", curPos
                htmlPos = curPos - 10
                newPos = f.seek(htmlPos, 0)
                print "New Position is: ", newPos
                f.write("||");


    # def handle_endtag(self, tag):
    #     # print "Found End Tag: ", tag
    def handle_data(self, data):
        strippedData = data.strip()
        if len(strippedData) > 0:
            print "What is the length: ", len(strippedData)
            print "We found some strippedData", strippedData
            print "Start Tag Text: \n", str(self.tempTag)
        self.tempTag = None

# for line in fileinput.input("regTester.html", inplace=True):


f = open(sys.argv[1], 'a+')
parser = myHParser()
# jsonfile = open(sys.argv[2], 'w')
# html = f.read().replace('\n', '')
f.seek(0,0)
html = f.read()

print html
parser.feed(html)

linenumber = parser.getpos()
print "The line number is: ", linenumber


f.close()

    
