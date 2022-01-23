from flask import Flask, render_template, request
import json
import requests
import os

url='https://commoditybucket.blob.core.windows.net/commodity-api/db.json'
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
            commodity_list = [
                {
                    'max_price': data[i]['max_price'],
                    'min_price': data[i]['min_price'],
                }
            ]
            return render_template('commodity.html', commodity_list=commodity_list)
            # print("Minimum Price one can get is ", data[i]['min_price'])
            # return 'Hello %s %s have fun learning python <br/> <a href="/">Back Home</a>' % (first_name, last_name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)