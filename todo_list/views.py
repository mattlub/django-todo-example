from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic

from .models import ToDoItem


def index(request):
	#import pdb; pdb.set_trace()
	
	if not request.user or not request.user.is_authenticated:
		return HttpResponse("please login!")
	
	user = request.user
	
	# if just added an item:
	if request.method == 'POST':
	# TODO: think about priority
		new_item = ToDoItem(
			description=request.POST['description'],
			priority=2,
			date_created=timezone.now(),
			user=user,
		)
		new_item.save()
		
		return HttpResponseRedirect("/")

	items = ToDoItem.objects.filter(user=user).order_by('-date_created')
	context = {
		'items': items,
		'user': user,
	}
	return render(request, "todo_list/index.html", context)

# could subclass django generic list view instead (here for reference)
class IndexView(generic.ListView):
	template_name = "todo_list/index.html"
	context_object_name = "items"
	
	def get_queryset(self):
		return ToDoItem.objects.all().order_by('-date_created')