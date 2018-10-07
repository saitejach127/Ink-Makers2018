# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

def get_audio_path(instance,filename):
	return 'audio/{0}/{1}'.format(instance.name, filename)

class Word(models.Model):
	url = models.CharField(max_length=255)
	image = models.URLField()
	name = models.CharField(max_length=255)
	audio = models.FileField(upload_to=get_audio_path, null=True, blank=True)

	def __str__(self):
		return self.name




