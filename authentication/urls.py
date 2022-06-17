from django.urls import path
from .views import RegisterView


urlpatterns =[

    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', RegisterView.as_view(), name="email_verify")
]