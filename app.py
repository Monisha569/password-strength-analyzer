from flask import Flask, render_template, request, jsonify
from password_analyzer import analyze_password, generate_password

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    password = data.get("password", "")

    result = analyze_password(password)

    return jsonify(result)


@app.route("/generate", methods=["GET"])
def generate():
    password = generate_password()

    return jsonify({
        "password": password
    })


if __name__ == "__main__":
    app.run(debug=True)