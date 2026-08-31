from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "wifi_bandwidth_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            zone = request.form["zone"]
            is_weekend = bool(int(request.form["is_weekend"]))
            is_exam = bool(int(request.form["is_exam"]))
            is_event = bool(int(request.form["is_event"]))
            avg_devices_connected = float(request.form["avg_devices_connected"])
            packet_loss_rate = float(request.form["packet_loss_rate"])
            day_of_week = int(request.form["day_of_week"])
            month = int(request.form["month"])
            rolling_avg_7 = float(request.form["rolling_avg_7"])

            new_data = pd.DataFrame({
                "zone": [zone],
                "is_weekend": [is_weekend],
                "is_exam": [is_exam],
                "is_event": [is_event],
                "avg_devices_connected": [avg_devices_connected],
                "packet_loss_rate": [packet_loss_rate],
                "day_of_week": [day_of_week],
                "month": [month],
                "rolling_avg_7": [rolling_avg_7]
            })

            result = model.predict(new_data)
            prediction = round(float(result[0]), 2)

        except Exception as e:
            error = f"Prediction error: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


@app.route("/about")
def about():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)