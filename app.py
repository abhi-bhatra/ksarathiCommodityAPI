from flask import Flask, render_template, request
import json
import requests

url='https://commodityapi.blob.core.windows.net/commodityapi/db.json'
r = requests.get(url)
data = json.loads(r.text)
total_length = len(data)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/commodity', methods=['POST'])
def hello():
    state = request.form['state']
    district = request.form['district']
    commodity = request.form['commodity']
    for i in range(total_length):
        if (state in data[i]['state']) and (district in data[i]['district']) and (commodity in data[i]['commodity']):
            return 'Maximum Price: %s and Minimum Price: %s <br/> <a href="/">Back Home</a> ' % (data[i]['max_price'], data[i]['min_price'])
            # print("Minimum Price one can get is ", data[i]['min_price'])
            # return 'Hello %s %s have fun learning python <br/> <a href="/">Back Home</a>' % (first_name, last_name)

if __name__ == '__main__':
    app.run(port = 5000)