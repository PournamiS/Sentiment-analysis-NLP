
from flask import Flask, render_template, request
from model import predict_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("interface.html")

@app.route("/input")
def input_page():
    return render_template("input.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["review"]
    result = predict_sentiment(text)
    return render_template("input.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
