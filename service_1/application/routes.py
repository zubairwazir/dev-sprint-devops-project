from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from . import app, db



@app.route('/')
def home():
    alc_drink = requests.get('http://service_2:5000/get/alc_drink').text 
    soft_drink = requests.get('http://service_3:5000/get/soft_drink').text 

    payload = {'alc_drink': alc_drink, 'soft_drink': soft_drink}
    price = requests.post('http://service_4:5000/post/round', json=payload).json()

    return render_template('home.html', price=price)









# return f"Your round has 1 {alc_drink} and a {soft_drink} for £{price}.\n"