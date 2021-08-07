from flask import Flask
import random

app = Flask(__name__)

alc_drink = ['Lager', 'Stout', 'Ale', 'Red Wine', 'White Wine', 'Spirits (Double)', 'Cocktails']

@app.route('/get/alc_drink', methods=['GET'])
def get_alc_drink():
    return random.choice(alc_drink)

if __name__ == '__main__':
    app.run(host='0.0.0.0')