from django import forms
from video_transcription_app.models import Video


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_url']


