🌾 Crop Recommendation System

Crop Recommendation System is a Machine Learning–based web application that predicts the most suitable crop to grow based on soil nutrients and environmental conditions. The application uses a trained classification model and provides predictions through an interactive Flask-based web interface.

Live Demo:- https://your-render-link.onrender.com/

🚀 Features
Crop recommendation based on soil and climate data
Machine Learning–based classification model
Fast and accurate predictions
User-friendly Flask web interface
REST API endpoint for predictions
Supports real-time form-based inputs
Lightweight and deployment-ready architecture

🛠️ Tech Stack
Language: Python  
Machine Learning: Scikit-learn  
Web Framework: Flask  
Data Handling: NumPy, Pandas  
Model Storage: Pickle (.pkl)  
Deployment: Render / Gunicorn  

▶️ How to Run the Project Locally

1️⃣ Clone the repository

git clone https://github.com/Pranav2100/Crop-Recommendation-System.git  
cd Crop-Recommendation-System  

2️⃣ Create and activate virtual environment

python -m venv venv  
venv\Scripts\activate  

3️⃣ Install dependencies

pip install -r requirements.txt  

4️⃣ Run the Flask application

python app.py  

Open browser and visit:  
http://127.0.0.1:5000  

🔗 API Usage

Endpoint:
POST /predict_api  

Sample Input:
{
  "data": {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.5,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 202
  }
}

Response:
"rice"

📊 Model Details

The model predicts the best crop based on:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Model trained using supervised machine learning techniques on agricultural datasets.

⚠️ Disclaimer

This project is created for educational and academic purposes only. Predictions should not be used as the sole basis for real-world agricultural decision-making.

👤 Author

Pranav Jagtap  

GitHub: https://github.com/Pranav2100  
LinkedIn: https://www.linkedin.com/in/pranav--jagtap  
Email: pranavjagtap2151@gmail.com