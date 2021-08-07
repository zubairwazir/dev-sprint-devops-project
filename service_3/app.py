from flask import Flask
import random

app = Flask(__name__)

soft_drinks = ['Water', 'Sparkling Water', 'Coca-Cola', 'Fanta', 'J2O', 'Tea', 'Coffee']

@app.route('/get/soft_drink', methods=['GET'])
def get_soft_drink():
    return random.choice(soft_drinks)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')