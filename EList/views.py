from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def StartPage(request):
	return render(request, 'index.html')
	#return HttpResponse('<html><title>Eljohn List</title></html>')
	#pass
#StartPage = None