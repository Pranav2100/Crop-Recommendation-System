import pickle
import os
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("croppredict.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json["data"]
    new_data = np.array(list(data.values())).reshape(1, -1)
    output = model.predict(new_data)
    return jsonify(output[0])

@app.route("/predict", methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)
    output = model.predict(final_input)[0]
    return render_template(
        "home.html",
        prediction_text=f"The crop that can be grown is {output}"
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
