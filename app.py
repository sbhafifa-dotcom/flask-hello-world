from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "FUTBIN bot is running - اكتب /futbin?name=Mbappe"

@app.route('/futbin')
def futbin():
    name = request.args.get('name', 'Mbappe')
    # مؤقتاً نرجع بيانات تجريبية لين نركب سكريبر FUTBIN
    # بعد ما يشتغل بنربطه مع FUTBIN الحقيقي
    return jsonify({
        "name": name,
        "price": "1,200,000",
        "rating": 91,
        "image": "https://cdn.futbin.com/content/fifa24/img/players/231747.png",
        "status": "ok"
    })

if __name__ == '__main__':
    app.run()
