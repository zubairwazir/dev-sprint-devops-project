from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'alc_drink': {
        'Lager': 0.00,
        'Stout': 0.00,
        'Ale': 0.00,
        'Red Wine': 0.00,
        'White Wine': 0.00,
        'Spirits (Double)': 0.00,
        'Cocktails': 0.00
    },
    'soft_drink': {
        'Water': 0.00,
        'Sparkling Water': 0.00,
        'Coca-Cola': 0.00,
        'Fanta': 0.00,
        'J20': 0.00,
        'Tea': 0.00,
        'Coffee': 0.00
    }
}

@app.route('/post/round', methods=['POST'])
def post_round():
    alc_drink = request.json['alc_drink']
    soft_drink = request.json['soft_drink']

    price = prices['alc_drink'][alc_drink] + prices['soft_drink'][soft_drink]
   

    return jsonify(price) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')