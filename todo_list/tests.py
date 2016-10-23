import datetime

from django.utils import timezone
from django.test import TestCase

from .models import ToDoItem


class ToDoItemMethodTests(TestCase):
	
	def test_was_created_recently_with_old_item(self):
		"""
		was_created_recently() should return False for old ToDoItem
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		old_item = ToDoItem(date_created=time)
		self.assertIs(old_item.was_created_recently(), False)
	

def create_todo_item(description, days=0, priority=2):
	date_created = timezone.now() - datetime.timedelta(days=days)
	return ToDoItem.objects.create(
		description=description,
		date_created=date_created,
		priority=priority
		)	

		
class ToDoItemViewTests(TestCase):
	
	def test_index_view_with_no_login(self):
		"""
		index view should return appropriate message if not logged in
		"""
		# TODO
	
	def test_index_view_with_no_items(self):
		"""
		index view should return appropriate message if no to do items
		"""
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Nothing to do!")
		self.assertQuerysetEqual(response.context["items"], [])
		
	def test_index_view_with_a_single_item(self):
		"""
		index view should return appropriate one-element list if only one to do item
		"""
		create_todo_item('test')
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["items"], ['<ToDoItem: test>'])
		
		
		