# WiFiPredict — Smart Campus Bandwidth Forecasting

<h1 align="center">404-FOUND-US</h1>
<p align="center"><em>Team</em></p>

Predict daily Wi‑Fi bandwidth usage across campus zones using a Random Forest regression model and a simple Flask web UI. Designed for quick experimentation and lightweight deployments (Vercel-friendly configuration included).

## Stack
- Language: Python
- Framework: Flask
- Notable libraries: scikit-learn, pandas, numpy

## Highlights
- Random Forest regression model (high R² on the evaluation notebook)
- Interactive web UI (fill network parameters and get an estimated daily bandwidth)
- Includes training notebook and dataset for inspection and retraining

## Quickstart
1. Clone the repo
   ```bash
   git clone https://github.com/Partho-Kumar-Shaw/samatrix-hackathon.git
   cd samatrix-hackathon
   ```
2. Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Run the app locally
   ```bash
   python app.py
   ```
4. Open http://localhost:5000/ in your browser. Use the Predict form to estimate bandwidth usage.

Note: The app expects `wifi_bandwidth_model.pkl` (already included). If the model file is missing the `/health` endpoint will indicate the error.

## Files you’ll care about
- `app.py` — Flask application and prediction endpoint
- `templates/index.html` & `static/style.css` — Web UI
- `wifi_bandwidth_model.pkl` — Trained model used by the app
- `bandwidth__prediction.ipynb` — Notebook with data exploration and model training
- `wifi_usage_data.csv` — Dataset used for training/evaluation
- `vercel.json` — config for deploying the app to Vercel

## Notes
- Health check: `GET /health` returns model load status and scikit-learn version.
- To retrain or explore: open `bandwidth__prediction.ipynb` and modify/retrain then export a new `.pkl` model.

---

Built with ❤️ by 404-FOUND-US — practical ML for campus networking
