from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np

# Load model
model = pickle.load(open("knn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))


# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("predict")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


# SIGNUP VIEW
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully")
            return redirect("login")

    return render(request, "signup.html")


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect("login")


# PREDICTION FORM VIEW
@login_required
def predict_view(request):

    if request.method == "POST":
        try:
            # 🔵 Convert inputs safely
            co = float(request.POST.get("co"))
            no2 = float(request.POST.get("no2"))
            so2 = float(request.POST.get("so2"))
            o3 = float(request.POST.get("o3"))
            pm25 = float(request.POST.get("pm25"))
            pm10 = float(request.POST.get("pm10"))

            # 🔵 Validation: Prevent negative values
            if any(value < 0 for value in [co, no2, so2, o3, pm25, pm10]):
                messages.error(request, "Pollutant values cannot be negative.")
                return render(request, "index.html")

        except (TypeError, ValueError):
            messages.error(request, "Please enter valid numeric values.")
            return render(request, "index.html")

        # 🔵 Prepare data
        input_data = np.array([[co, no2, so2, o3, pm25, pm10]])
        input_scaled = scaler.transform(input_data)

        # 🔵 Predict
        result = model.predict(input_scaled)
        prediction = le.inverse_transform(result)[0]

        # 🔵 Confidence Score
        probabilities = model.predict_proba(input_scaled)
        confidence = round(np.max(probabilities) * 100, 2)

        # 🔵 AQI Explanation (Only 2 Classes)
        explanations = {
            "industrial": (
                "This area is classified as Industrial. "
                "Pollution levels are typically higher due to industrial emissions. "
                "Sensitive individuals should limit prolonged outdoor exposure."
            ),
            "residential": (
                "This area is classified as Residential. "
                "Air quality is comparatively better with lower industrial impact. "
                "Health risk is generally lower for most people."
            )
        }

        explanation = explanations.get(
            prediction.lower(),
            "Air quality category detected."
        )

        # 🔵 Store in session
        request.session['prediction'] = prediction
        request.session['confidence'] = confidence
        request.session['explanation'] = explanation
        request.session['co'] = co
        request.session['no2'] = no2
        request.session['so2'] = so2
        request.session['o3'] = o3
        request.session['pm25'] = pm25
        request.session['pm10'] = pm10

        return redirect("result")

    return render(request, "index.html")


# RESULT PAGE VIEW
@login_required
def result_view(request):

    return render(request, "result.html", {
        "prediction": request.session.get("prediction"),
        "confidence": request.session.get("confidence"),
        "explanation": request.session.get("explanation"),
        "co": request.session.get("co", 0),
        "no2": request.session.get("no2", 0),
        "so2": request.session.get("so2", 0),
        "o3": request.session.get("o3", 0),
        "pm25": request.session.get("pm25", 0),
        "pm10": request.session.get("pm10", 0),
    })
