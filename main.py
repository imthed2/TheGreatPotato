from flask import Flask, send_file
import requests
from bs4 import BeautifulSoup
import random
import io

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sora Random Image API is running!'

@app.route('/random')
def random_image():
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get('https://sora.chatgpt.com/explore', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    img_tags = soup.find_all('img')
    image_urls = [tag['src'] for tag in img_tags if tag.get('src') and tag['src'].startswith('https://')]

    if not image_urls:
        return "No images found", 404

    chosen_image = random.choice(image_urls)
    img_response = requests.get(chosen_image)

    return send_file(io.BytesIO(img_response.content), mimetype='image/jpeg')
