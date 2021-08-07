from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'alc_drink': {
        'Lager': 4.00,
        'Stout': 3.50,
        'Ale': 4.50,
        'Red Wine': 7.50,
        'White Wine': 6.50,
        'Spirits (Double)': 6.75,
        'Cocktails': 7.95
    },
    'soft_drink': {
        'Water': 0.00,
        'Sparkling Water': 1.50,
        'Coca-Cola': 2.15,
        'Fanta': 2.00,
        'J20': 2.50,
        'Tea': 3.50,
        'Coffee': 3.00
    }
}

@app.route('/post/round', methods=['POST'])
def post_round():
    alc_drink = request.json['alc_drink']
    soft_drink = request.json['soft_drink']

    price = prices['alc_drink'][alc_drink] + prices['soft_drink'][soft_drink]
    price = round(price, 2)

    return jsonify(price) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')