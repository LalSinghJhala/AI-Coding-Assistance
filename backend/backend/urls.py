from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # <- Needed!

# Add a simple home page view
def home(request):
    return HttpResponse("Hello! Django is working.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chatbot.urls')),  # your API routes
    path('', home),  # <-- root path now points to 'home'
]
