#3&4th Exercise
from flask import Flask,jsonify
import json
app = Flask(__name__)
@app.route('/airport/<code>')
def airport(code):
    with open('airports.json','r') as f:
        data = json.load(f)
        if code not in data:
            return jsonify('404 error')
        else:
            store_code = {
                'icao':data[code]['icao'],
                'name':data[code]['name'],
                'city':data[code]['city'],
                'country':data[code]['country']
            }
    return jsonify(store_code)
@app.route('/prime_number/<number>')
def prime_number(number):
    up_num = float(number)
    if up_num <= 2:
        return jsonify('Prime number')
    else:
        for i in range(2,int(up_num**0.5)):
            if up_num % i == 0:
                return jsonify('Not prime number')
        return jsonify('Prime number')
if __name__ == '__main__':
    app.run(host='127.0.0.1',port = 5000)
