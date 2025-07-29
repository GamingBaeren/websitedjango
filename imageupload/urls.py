from django.urls import path
from . import views

app_name = 'imageupload'

urlpatterns = [
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:image_id>/', views.image_detail, name='image_detail'),
]
