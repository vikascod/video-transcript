from django.shortcuts import render, redirect
from video_transcription_app.models import Video
from video_transcription_app.forms import VideoUploadForm
import os
import requests
import speech_recognition as sr
import subprocess

def transcribe_video(request):
    form = VideoUploadForm()
    if request.method == "POST":
        form = VideoUploadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']

            # download the video and save it to the working directory
            response = requests.get(video_url)
            open("video.mp4", "wb").write(response.content)
            print("Downloaded")
            #Extract audio
            command = 'ffmpeg -y -i video.mp4 -ab 160k -ar 44100 -vn audio.wav'
            subprocess.call(command, shell=True)

            filename = "audio.wav"

            r = sr.Recognizer()

            # use the AudioFile class to open the audio file
            with sr.AudioFile(filename) as source:
                # read the audio data from the file
                audio_data = r.record(source)
                
                # recognize the speech in the audio file
                text = r.recognize_google(audio_data)
                
            video = Video(video_url=video_url, transcript=text)
            video.save()

            return redirect('transcript_result', pk=video.pk)

    context = {'form':form}
    return render(request, 'transcribe_video.html', context)


def transcript_result(request, pk):
    video = Video.objects.get(pk=pk)
    context = {'video': video}
    return render(request, 'transcription_result.html', context)
