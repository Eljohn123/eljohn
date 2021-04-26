from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def StartPage(request):
	return render(request, 'index.html', {
		'new_item_text': request.POST.get('item_text', ''),
		})
def ListPage(request):
	return render(request, 'diarylist.html')
	#return HttpResponse('<html><title>Eljohn List</title></html>')
	#pass
#StartPage = None