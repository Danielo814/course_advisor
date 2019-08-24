#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
from request import get_tee_times

def extract():
    tee_times = get_tee_times('https://hardingparkstarter1sdfij.ezlinks.com/(X(1)S(ivvd3i4z3iyqhzimx3gt1zdh))/Facility/ViewTeeSheet.aspx?AspxAutoDetectCookieSupport=1')
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('index.html')
    output = template.render()
    print(output)

extract()