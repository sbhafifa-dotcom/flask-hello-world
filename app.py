from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "FUTBIN bot is running - جرب /futbin?name=Mbappe"

@app.route('/futbin')
def futbin():
    name = request.args.get('name', 'Mbappe')
    try:
        # نبحث في FUTBIN
        url = f"https://www.futbin.com/search?year=26&term={name}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        r = requests.get(url, headers=headers, timeout=15)
        data = r.json()

        if data and len(data) > 0:
            player = data[0]
            player_id = player.get('id')

            # نجيب سعره الحقيقي
            price_url = f"https://www.futbin.com/26/player/{player_id}"
            r2 = requests.get(price_url, headers=headers, timeout=15)
            soup = BeautifulSoup(r2.text, 'html.parser')

            # نحاول نجيب السعر
            price_tag = soup.find('div', {'id': 'ps-lowest-1'})
            price = price_tag.text.strip() if price_tag else player.get('ps_price', '1,200,000')

            return jsonify({
                "name": player.get('name'),
                "price": price,
                "rating": player.get('rating'),
                "image": f"https://cdn.futbin.com/content/fifa26/img/players/{player_id}.png",
                "status": "ok"
            })
    except Exception as e:
        print(e)
        pass

    return jsonify({
        "name": name,
        "price": "1,200,000",
        "rating": 91,
        "image": "https://cdn.futbin.com/content/fifa24/img/players/231747.png",
        "status": "demo"
    })

if __name__ == '__main__':
    app.run()
