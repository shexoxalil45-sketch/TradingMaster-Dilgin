# TradingMaster-Dilgin - Main App
# Version 1.0 | Multi-platform | Multi-language
# Author: Dilgin (via ChatGPT setup)
# Safe demo framework – does NOT handle real funds by default

from flask import Flask, render_template_string, request, jsonify
import random, time

app = Flask(__name__)

# -----------------------------
# واجهة بسيطة فيها لغتين EN / AR
# -----------------------------
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TradingMaster - Dilgin</title>
<style>
body { font-family: sans-serif; text-align:center; background:#101010; color:#fff; }
button { background:#00c896; color:#fff; border:none; padding:12px 24px; margin:10px; border-radius:10px; font-size:18px; }
.card { background:#1d1d1d; margin:20px auto; padding:20px; width:90%; max-width:500px; border-radius:15px; }
</style>
</head>
<body>
<h1>🤖 TradingMaster - Dilgin</h1>
<p>اختر اللغة | Choose Language</p>
<button onclick="setLang('ar')">العربية</button>
<button onclick="setLang('en')">English</button>
<div class="card" id="content"></div>

<script>
let lang = 'ar';
function setLang(l) {
  lang = l;
  document.getElementById("content").innerHTML = (l === 'ar')
    ? `<h2>مرحبًا دِلغين!</h2><p>ابدأ التداول التجريبي بأمان.<br>عندما تكون جاهزًا، يمكنك تفعيل الحساب الحقيقي بسهولة.</p>
       <button onclick="startDemo()">ابدأ التداول التجريبي</button>`
    : `<h2>Welcome, Dilgin!</h2><p>Start safe demo trading.<br>When ready, you can switch to live mode.</p>
       <button onclick="startDemo()">Start Demo Trading</button>`;
}

function startDemo() {
  fetch('/demo').then(res=>res.json()).then(d=>{
    document.getElementById("content").innerHTML = (lang==='ar')
      ? `<h2>📈 صفقة تجريبية</h2><p>الزوج: ${d.pair}<br>الإشارة: ${d.signal}</p>`
      : `<h2>📈 Demo Trade</h2><p>Pair: ${d.pair}<br>Signal: ${d.signal}</p>`;
  });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/demo")
def demo_trade():
    pairs = ["BTC/USDT", "ETH/USDT", "XRP/USDT", "SOL/USDT"]
    signals = ["Buy 🔼", "Sell 🔽", "Wait ⏸️"]
    data = {
        "pair": random.choice(pairs),
        "signal": random.choice(signals)
    }
    return jsonify(data)

if __name__ == "__main__":
    print("✅ Running TradingMaster (demo mode) on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
