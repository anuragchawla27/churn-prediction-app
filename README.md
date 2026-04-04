🚀 Customer Churn Prediction App

A full-stack Machine Learning project that predicts whether a customer will churn or not using a trained classification model.

This project integrates a FastAPI backend with a Streamlit frontend and is fully deployed online.

🌐 Live Demo
🔗 Frontend (Streamlit App)

https://anurag-churn-predictor.streamlit.app/

🔗 Backend API (FastAPI Docs)

https://churn-api-xa9z.onrender.com/docs

📌 Project Overview

Customer churn prediction is crucial for businesses to retain customers.

This app allows users to input customer details and get real-time predictions.

💡 Features:

Interactive UI using Streamlit

Real-time prediction via API

FastAPI backend for ML model serving

Fully deployed (Render + Streamlit Cloud)

🧠 Tech Stack

Frontend: Streamlit

Backend: FastAPI, Uvicorn

Machine Learning: Scikit-learn

Libraries: Pandas, NumPy

Deployment: Render, Streamlit Cloud

⚙️ How It Works

User enters customer details in Streamlit UI

Request is sent to FastAPI backend

Backend processes input and runs ML model

Prediction is returned and displayed

📂 Project Structure

churn-prediction-app/
│
├── app.py                # Streamlit frontend
├── main.py               # FastAPI backend
├── model.pkl             # Trained ML model
├── scaler.pkl            # Scaler used in preprocessing
├── requirements.txt      # Dependencies
└── README.md

🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/anuragchawla27/churn-prediction-app.git

cd churn-prediction-app

3. Install Dependencies

👉 For Frontend (Streamlit)

4. pip install streamlit requests

👉 For Backend (FastAPI)

5. pip install fastapi uvicorn scikit-learn pandas numpy

Run Backend Locally

5.uvicorn main:app --reload

👉 Open in browser:

http://127.0.0.1:8000/docs

6. Run Frontend Locally

streamlit run app.py

📦 API Endpoint

POST /predict

Input Example:

{

  "tenure": 12,
  
  "MonthlyCharges": 70.5,
  
  "TotalCharges": 850.0
  
}

Output:

{

  "prediction": "Churn"
  
}


🚀 Future Improvements
Add MLflow for experiment tracking
Add Docker support
CI/CD pipeline

👨‍💻 Author

Anurag Chawla

GitHub: https://github.com/anuragchawla27
If you like this project

Give it a ⭐ on GitHub and share it!
