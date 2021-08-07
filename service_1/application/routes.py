from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    alc_drink = requests.get('http://service_2:5000/get/alc_drink').text 
    soft_drink = requests.get('http://service_3:5000/get/soft_drink').text 

    payload = {'alc_drink': alc_drink, 'soft_drink': soft_drink}
    price = requests.post('http://service_4:5000/post/round', json=payload).json()

    return f"Your round has {alc_drink} and a {soft_drink} for £{price}.\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)