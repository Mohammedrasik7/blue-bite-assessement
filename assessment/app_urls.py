from django.urls import path
from .views import create_batch, retrieve_object, list_objects

# URL patterns for the assessment application
urlpatterns = [
    path('api/objects/', create_batch, name='create_batch'),
    path('api/object/<str:object_id>/', retrieve_object, name='retrieve_object'),
    path('api/list-objects/', list_objects, name='list_objects'),
    ]
