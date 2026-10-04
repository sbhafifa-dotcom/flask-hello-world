from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
CORS(app)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.futbin.com/"
}

@app.route("/")
def home():
    return "FUTBIN BOT IS LIVE - Use /futbin?name=Mbappe"

@app.route("/futbin")
def get_price():
    name = request.args.get("name", "Mbappe")
    
    try:
        # 1- نبحث عن اللاعب
        search_url = f"https://www.futbin.com/search?year=26&term={name}"
        r = requests.get(search_url, headers=HEADERS, timeout=10)
        
        # نحاول نطلع اول لاعب
        if "
