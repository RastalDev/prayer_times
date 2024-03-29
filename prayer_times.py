#!/usr/bin/env python3

# Author: https://github.com/RastalDev
# A Python script to show Islamic prayer times scraped from url

# Modules to be used in the script
import urllib.request
from html_table_parser.parser import HTMLTableParser
import pandas as pd

# Function to open the website and read
def contents(url):
    req_site = urllib.request.Request(url)
    open_site = urllib.request.urlopen(req_site)
    return open_site.read()

# Define html objects, feed to table parser and get data of table
web_html = contents('https://timesprayer.com/en/prayer-times-in-city-of-westminster.html').decode('utf-8')
htp = HTMLTableParser()
htp.feed(web_html)

# Convert data to dataframe
print("Prayer Timetable\n")
print(pd.DataFrame(htp.tables[0]))
