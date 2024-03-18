from django.urls import path
from . import views

urlpatterns = [
    path('reminder/', views.reminder, name='reminder'),
]


##In this urls.py file, we’re defining a route for our reminder view. When a POST request is sent to ‘/reminder/’, Django will call the reminder function in views.py.
