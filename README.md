🌍 Air Quality Prediction System

An end-to-end Machine Learning web application that predicts Air Quality Index (AQI) levels based on environmental parameters.

This project includes complete data preprocessing, model training, backend development, frontend integration, and database connectivity.

🚀 Project Overview

The Air Quality Prediction System uses a K-Nearest Neighbors (KNN) algorithm to analyze pollutant data and predict AQI levels.

The application is built using Django for backend processing and provides a simple user interface for real-time AQI prediction.

🧠 Machine Learning Workflow

Data Collection (air_quality.csv)

Data Cleaning & Preprocessing

Feature Scaling using StandardScaler

Label Encoding

Model Training using KNN

Model Serialization using Pickle (.pkl files)

Integration with Django backend

📌 Features

✔ AQI Prediction using trained ML model
✔ Clean and structured dataset handling
✔ Model saving and loading (.pkl)
✔ Django-based backend
✔ Interactive frontend UI
✔ SQLite database integration
✔ Organized project structure

🛠 Tech Stack
Programming Language

Python

Machine Learning

Scikit-learn

Pandas

NumPy

Backend Framework

Django

Frontend

HTML

CSS

Database

SQLite

📂 Project Structure
Air_Quality_Prediction/
│
├── air_quality_project/      # Main Django project
├── predictor/                # Django app for prediction logic
├── static/images/            # Static files
├── air_quality.csv           # Dataset
├── train_model.py            # ML model training script
├── knn_model.pkl             # Saved trained model
├── scaler.pkl                # Feature scaler
├── label_encoder.pkl         # Label encoder
├── manage.py                 # Django management file
├── db.sqlite3                # Database file
└── app.py                    # Application logic
⚙️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/ArchanaAN2353/Air_Quality_Prediction.git
2️⃣ Navigate to Project Folder
cd Air_Quality_Prediction
3️⃣ Install Dependencies
pip install -r requirements.txt

(If requirements.txt is not available, install Django and required ML libraries manually.)

4️⃣ Run the Server
python manage.py runserver

Then open:

http://127.0.0.1:8000/
🎯 Objective

To build an intelligent AQI prediction system that helps analyze environmental conditions and supports data-driven pollution monitoring.

📈 Future Improvements

Deploy on cloud (Render / Railway)

Add real-time API integration

Improve model accuracy using advanced algorithms

Add data visualization dashboard

👩‍💻 Developed By

Archana A N
