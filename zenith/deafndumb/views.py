# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Word
from gtts import gTTS 

# Create your views here.

def index(request):
	word = Word.objects.all()
	print(word)
	response = {}
	response['word'] = word
	return render(request, "deafndumb/index.html", response)

def home(request):
	response = {}
	if request.method == "POST":
		given_word = request.POST["word"]
		try:
			word = Word.objects.get(name=given_word)
			response["word"] = word
			print(word)
			return render(request, "deafndumb/home.djt", response)
		except:
			response["error"] = "Sorry Word Not Found"
			return render(request, "deafndumb/home.djt", response)

	return render(request, "deafndumb/home.djt", response)

def text2speech(request):
	response = {}
	if request.method == "POST":
		given_word = request.POST["word"]
		mytext = str(given_word)
		language = 'en'
		myobj = gTTS(text=mytext, lang=language, slow=False)
		myobj.save("media/t2s/speech.mp3")
		response["success"] = True
		return render(request, "deafndumb/t2s.html", response)

	return render(request, "deafndumb/t2s.html", response)



