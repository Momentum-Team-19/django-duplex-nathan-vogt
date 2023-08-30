from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

urlpatterns = [
    # ... your other url patterns
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', include('registration.backends.simple.urls')),
]

