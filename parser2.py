import fileinput
from HTMLParser import HTMLParser
import sys, re

class myHParser(HTMLParser):
    tempTag = None
    hasLocale = False
    quick_help_array = []
    inner_html_array = []
        
    def print_quick_help(self):
        print 'WELCOME TO THE THUNDER DOME\n'
        print '--------------------'
        print "Quick Help Found: ", len(self.quick_help_array)
        for q in self.quick_help_array:
            print "-->", q
        print '--------------------'

    def print_inner_html(self):
        print '--------------------'
        print "Inner HTML Found: ", len(self.inner_html_array)
        for h in self.inner_html_array:
            print "-->", h


    def handle_starttag(self, tag, attrs):
        hasLocale = False
        self.tempTag = tag;
        for a in attrs:
            if a[0] == 'data-quickhelp':
                self.quick_help_array.append(a[1])


    # def handle_endtag(self, tag):
    #     # print "Found End Tag: ", tag
    def handle_data(self, data):
        strippedData = data.strip()
        if len(strippedData) > 0:
            self.inner_html_array.append(strippedData)
        self.tempTag = None

# for line in fileinput.input("regTester.html", inplace=True):


f = open(sys.argv[1], 'r')
parser = myHParser()
# jsonfile = open(sys.argv[2], 'w')
# html = f.read().replace('\n', '')
html = f.read()

parser.feed(html)

parser.print_quick_help()
parser.print_inner_html()
f.close()
