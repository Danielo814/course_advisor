#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
from request import get_tee_times
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def fill(): 
    tee_times = get_tee_times('https://hardingparkstarter1sdfij.ezlinks.com/(X(1)S(ivvd3i4z3iyqhzimx3gt1zdh))/Facility/ViewTeeSheet.aspx?AspxAutoDetectCookieSupport=1')
    # file_loader = FileSystemLoader('templates')
    # env = Environment(loader=file_loader)
    # template = env.get_template('index.html')
    name1 = tee_times['3:00 pm'][0]
    name2 = tee_times['3:10 pm'][1]
    name3 = tee_times['3:20 pm'][2]
    name4 = tee_times['3:30 pm'][3]

    return render_template('index.html', name1=name1, name2=name2, name3=name3, name4=name4)

if __name__ == '__main__':
    app.run()