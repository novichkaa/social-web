from django.urls import path
from .views import SignUpView, upload_images

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('upload_images/',upload_images, name = "images" )
]