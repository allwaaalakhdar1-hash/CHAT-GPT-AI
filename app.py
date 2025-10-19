import os

from flask import Flask, request, jsonify, render_template
import openai
import requests
from langdetect import detect

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

woocommerce_url = os.getenv(
    "WOOCOMMERCE_URL", "https://YOUR-WOOCOMMERCE-URL.com/wp-json/wc/v3/products"
)
consumer_key = os.getenv("WOOCOMMERCE_CONSUMER_KEY", "YOUR_WC_CONSUMER_KEY")
consumer_secret = os.getenv("WOOCOMMERCE_CONSUMER_SECRET", "YOUR_WC_CONSUMER_SECRET")
google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

def search_products(query):
    params = {
        "search": query,
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret
    }
    response = requests.get(woocommerce_url, params=params)
    if response.status_code == 200:
        products = response.json()
        return [f"{p['name']} - {p['price']}" for p in products]
    else:
        return ["❌ لا يمكن الوصول إلى المنتجات."]

@app.route("/")
def map_view():
    """Render the multi-stop delivery planning map."""
    return render_template("map.html", google_maps_api_key=google_maps_api_key)


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    lang = detect(user_input)

    prompt = (
        f"الرد على هذا السؤال كموظف مبيعات: {user_input}"
        if lang == "ar"
        else f"Act as a helpful store assistant. Question: {user_input}"
    )

    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = gpt_response.choices[0].message.content

    if "product" in user_input.lower() or "منتج" in user_input:
        products = search_products(user_input)
        reply += "\n\n🛍️ منتجات مقترحة:\n" + "\n".join(products[:5])

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
