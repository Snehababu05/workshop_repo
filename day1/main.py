from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
  data = [
    {
      "name" : "James",
      "link" : "https://media4.giphy.com/media/10Bb1Bq7BMi9Co/200w.webp"  
  },
  {
    "name" : "John",
    "link" : "https://media4.giphy.com/media/10Bb1Bq7BMi9Co/200w.webp"
  }]

  return jsonify(data)

app.run(debug=True)
