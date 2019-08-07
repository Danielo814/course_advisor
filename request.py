#!/usr/bin/python3
"""
Module to scrape tee sheet data from HTMl form
"""

from bs4 import BeautifulSoup
import requests
import time

def get_tee_times(link):
    new_dict = {}
    arr = []
    req = requests.get(link)
    soup = BeautifulSoup(req.text, features="lxml")
    # with open("data.html" , "w") as fd:
    #     fd.write(soup.prettify())
    # soup = BeautifulSoup("<html>data</html>", features="lxml")
    rows = soup.findAll('tr')
    for row in rows:
        columns = row.findAll('td')
        for column in columns:
            if row.has_attr('class') and column.has_attr('width'):
                arr.append(column.contents[0])
    i = 0
    while i < len(arr) - 4:
        new_dict[arr[i]] = [arr[i + 1], arr[i + 2], arr[i + 3], arr[i + 4]]
        i += 5
    print(new_dict)

get_tee_times('https://hardingparkstarter1sdfij.ezlinks.com/(X(1)S(ivvd3i4z3iyqhzimx3gt1zdh))/Facility/ViewTeeSheet.aspx?AspxAutoDetectCookieSupport=1')
