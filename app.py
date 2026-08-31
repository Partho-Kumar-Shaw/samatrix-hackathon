
from flask import Flask, render_template, request
import os
import pickle
import pandas as pd
import sklearn

app = Flask(__name__)

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "wifi_bandwidth_model.pkl"
)

model = None
model_error = None


# Load the trained model
try:
    print("========================================")
    print("Loading WiFi bandwidth model...")
    print("Model path:", MODEL_PATH)
    print("scikit-learn version:", sklearn.__version__)
    print("pandas version:", pd.__version__)
    print("========================================")

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    print("Model loaded successfully.")

except Exception as e:
    model_error = (
        f"Model loading failed: {type(e).__name__}: {str(e)}"
    )

    print("========================================")
    print("MODEL LOADING ERROR")
    print(model_error)
    print("========================================")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = model_error

    if request.method == "POST":
        try:
            # Make sure the model was loaded
            if model is None:
                raise Exception(
                    model_error or "Model could not be loaded."
                )

            # Get form data
            zone = request.form["zone"]

            is_weekend = bool(
                int(request.form["is_weekend"])
            )

            is_exam = bool(
                int(request.form["is_exam"])
            )

            is_event = bool(
                int(request.form["is_event"])
            )

            avg_devices_connected = float(
                request.form["avg_devices_connected"]
            )

            packet_loss_rate = float(
                request.form["packet_loss_rate"]
            )

            day_of_week = int(
                request.form["day_of_week"]
            )

            month = int(
                request.form["month"]
            )

            rolling_avg_7 = float(
                request.form["rolling_avg_7"]
            )

            # Create DataFrame with the same feature names
            # used during model training
            new_data = pd.DataFrame({
                "zone": [zone],
                "is_weekend": [is_weekend],
                "is_exam": [is_exam],
                "is_event": [is_event],
                "avg_devices_connected": [
                    avg_devices_connected
                ],
                "packet_loss_rate": [
                    packet_loss_rate
                ],
                "day_of_week": [day_of_week],
                "month": [month],
                "rolling_avg_7": [rolling_avg_7]
            })

            print("Prediction input:")
            print(new_data)

            # Make prediction
            result = model.predict(new_data)

            prediction = round(float(result[0]), 2)
            error = None

            print("Prediction:", prediction)

        except Exception as e:
            error = (
                f"Prediction error: "
                f"{type(e).__name__}: {str(e)}"
            )

            print(error)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/health")
def health():
    """
    Simple endpoint to verify that the Vercel deployment
    is running and whether the model loaded successfully.
    """
    if model is not None:
        return {
            "status": "ok",
            "model_loaded": True,
            "sklearn_version": sklearn.__version__
        }

    return {
        "status": "error",
        "model_loaded": False,
        "error": model_error,
        "sklearn_version": sklearn.__version__
    }, 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )

