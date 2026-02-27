import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("air_quality.csv")

X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']]
y = data['Area_Type']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Train Model
knn = KNeighborsClassifier(n_neighbors=5, metric='manhattan', weights='distance')
knn.fit(X_train, y_train)

# -----------------------------
# Frontend UI
# -----------------------------
st.title("🌍 Air Quality Area Type Prediction")

st.write("Enter Pollution Values Below:")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")

if st.button("Predict Area Type"):

    user_data = pd.DataFrame([[pm25, pm10, no2, so2, co, o3]],
                             columns=['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])

    user_data = scaler.transform(user_data)

    prediction = knn.predict(user_data)

    st.success(f"Predicted Area Type: {prediction[0]}")
