#!/usr/bin/python

#import sys, getopt
from bs4 import BeautifulSoup
import os
import requests

USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')

if not USER :
    print "can't find USER system variable"
    exit(1)

if not PASSWORD:
    print "can't find PASSWORD system variable"
    exit(1)

def main():
      r = requests.get("https://mirantis.jira.com/wiki/display/PRT/Hardware+for+PI+team", auth=(USER, PASSWORD))
      if r.status_code != 200:
          print "can't get content"
          exit(1) 
      html_data = r.text

      table_data = [[cell.text for cell in row("td")]
                               for row in BeautifulSoup(html_data,"html5lib")("tr")]
      
      for item in table_data:
          if item:
            print u"{} {}".format(item[0], item[4]).encode('ascii','ignore')

if __name__ == "__main__":
   main()
