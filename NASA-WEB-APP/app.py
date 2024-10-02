import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

# Nasa API KEY
NASA_API_KEY = "rLRKUXWfw4ovsAi6uHCvT9wEsJxrIZz9sSTSsuxU"

@app.route('/')
def index():
      return render_template('index.html')

@app.route("/apod", methods = ['GET'])
def get_apod():
      nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
      response = requests.get(nasa_url)
      data = response.json()
      return render_template('apod.html', data=data)


if __name__ == "__main__":
      app.run(debug=True)

