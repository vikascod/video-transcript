from django.urls import path
from .views import transcribe_video, transcript_result

urlpatterns = [
    path('', transcribe_video, name='transcribe_video'),
    path('transcript-result/<int:pk>/', transcript_result, name='transcript_result'),
]
