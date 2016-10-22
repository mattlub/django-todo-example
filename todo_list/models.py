from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class ToDoItem(models.Model):
	
	HIGH = 3
	MEDIUM = 2
	LOW = 1
	PRIORITY_CHOICES = (
		(HIGH, 'High'),
		(MEDIUM, 'Medium'),
		(LOW, 'Low'),
	)
	
	description = models.CharField(max_length=100)
	date_created = models.DateTimeField()
	completed = models.BooleanField(default=False)
	priority = models.IntegerField(choices=PRIORITY_CHOICES)
	
	def __unicode__(self):
		return self.description
		
	def was_created_recently(self):
		return self.date_created >= timezone.now() - datetime.timedelta(days=2)