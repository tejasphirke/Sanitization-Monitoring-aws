from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    names = ['akshay','bhikan','sandeep','tejas']
    date = []
    for i in names:
        url = "https://7bwcdzfj44.execute-api.us-east-1.amazonaws.com/sanitizerappretrieve?Name="+i
        resp = requests.get(url)
        data = resp.json()
        print(data)
        #[{'name': 'sandeep', 'date': '31-09-2020'}]
        date.append(data['date'])
    return render_template('stats.html', p1= names[0],d1=date[0], p2=names[1], d2=date[1],p3=names[2], d3=date[2],p4=names[3], d4=date[3])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)