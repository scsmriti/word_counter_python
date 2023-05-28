import requests
import operator
import re
from collections import Counter
from flask import Flask, render_template, request, json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=[ 'GET', 'POST'])

def freq_counter():
      
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        
            url = request.form['url']
            p = requests.get(url)
           
    
            raw = BeautifulSoup(p.text, 'html.parser').get_text()
            raw=raw.lower()
            text = re.sub("[^\w ]", " ", raw)
            text=text.split(" ")
            text= list(filter(lambda x:x!='',text))
            results = Counter(text)
       
    return render_template('freq_counter.html', results=json.dumps(results))

if __name__ == '__main__':
    app.run()