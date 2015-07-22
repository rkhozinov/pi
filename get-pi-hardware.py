#!/usr/bin/python

from bs4 import BeautifulSoup
import os
import requests

user=os.getenv('USER')
password=os.getenv('PASSWORD')
url = "https://mirantis.jira.com/wiki/display/PRT/Hardware+for+PI+team"

if not user :
    print "can't find user system variable"
    exit(1)

if not password:
    print "can't find password system variable"
    exit(1)

def main():
    r = requests.get(url, auth=(user, password))
    if r.status_code != 200:
        print "can't get content"
        exit(1) 
    
    html_data = r.text

    table_data = [[cell.text for cell in row("td")]
                             for row in BeautifulSoup(html_data, "html5lib")("tr")]
    
    for item in table_data:
        if item:
          print u"{} {}".format(item[0], item[4]).encode('ascii', 'ignore')

if __name__ == "__main__":
   main()
