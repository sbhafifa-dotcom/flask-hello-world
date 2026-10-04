from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html dir='rtl' style='font-family:sans-serif; text-align:center; padding:40px'>
    <h1 style='color:green'>✅ بوت FUTBIN شغال!</h1>
    <p>السيرفر شغال 100%</p>
    <a href='/sbc' style='background:#000;color:#fff;padding:15px 30px;text-decoration:none;border-radius:8px;display:inline-block;margin-top:20px'>روح لتحديات SBC</a>
    </html>
    """

@app.route('/sbc')
def sbc():
    try:
        url = "https://www.futbin.com/squad-building-challenges"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        return f"""
        <h2>اتصلنا بـ FUTBIN ✅</h2>
        <p>Status: {r.status_code}</p>
        <p>البوت جاهز يسحب التحديات</p>
        <a href='/'>رجوع</a>
        """
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run()
