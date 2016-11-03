from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.views.decorators.cache import never_cache

from .models import ToDoItem

@never_cache
def index(request):
	
	if not request.user or not request.user.is_authenticated:
		return HttpResponse("please login!")
	
	user = request.user
	
	# if POST request:
	if request.method == 'POST':

		if request.POST.get('class', None) == "Add":
			# TODO: think about priority
			new_item = ToDoItem(
				description=request.POST.get('description', None),
				priority=2,
				date_created=timezone.now(),
				user=user
			)
			new_item.save()
			return HttpResponseRedirect("/")
		
		# works now the request comes as form data. otherwise use request.body
		elif request.POST.get('class', None) == "Remove":
			completed_item = ToDoItem.objects.get(id=request.POST.get('id', None))
			if not completed_item:
				# should raise error
				return HttpResponseRedirect("/")
			completed_item.completed = True 
			completed_item.save()
			return HttpResponseRedirect("/")
			
	# else not POST request
	items = ToDoItem.objects.filter(user=user, completed=False).order_by('-date_created')
	# import pdb; pdb.set_trace()
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