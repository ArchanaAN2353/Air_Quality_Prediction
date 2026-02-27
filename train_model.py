import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Load your dataset
data = pd.read_csv("air_quality.csv")

# Preview the data
print(data.head())
print(data.info())
# Handle missing values (drop or fill)
data = data.dropna()  # or use data.fillna(data.mean(), inplace=True)

# Encode categorical target variable
label_encoder = LabelEncoder()
data['AQI_Category'] = label_encoder.fit_transform(data['AQI_Category'])

# Split features and target
X = data.drop('AQI_Category', axis=1)
y = data['AQI_Category']

# Scale features for KNN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
# Initialize KNN
knn = KNeighborsClassifier(n_neighbors=5)  # You can tune n_neighbors

# Train model
knn.fit(X_train, y_train)
# Predict on test data
y_pred = knn.predict(X_test)

# Accuracy and metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
# Example: New air quality readings
new_data = np.array([[120, 200, 50, 15, 1.2, 70]])  # PM2.5, PM10, NO2, SO2, CO, O3
new_data_scaled = scaler.transform(new_data)
prediction = knn.predict(new_data_scaled)
predicted_category = label_encoder.inverse_transform(prediction)

print("Predicted AQI Category:", predicted_category[0])
