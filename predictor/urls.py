from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('predict/', views.predict_view, name='predict'),  # input form page
    path('result/', views.result_view, name='result'),    # result page
]
