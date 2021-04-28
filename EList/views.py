from django.shortcuts import redirect,render
from django.http import HttpResponse
from EList.models import Item
# Create your views here.
def StartPage(request):
	#item = Item()
	#item.text = request.POST.get('item_text', '')
	#item.save()
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
		#new_item_text = request.POST['item_text']
		#Item.objects.create(text=new_item_text)
	#else:
		#new_item_text = ''
	items = Item.objects.all()
	return render(request, 'index.html', {'items' : items})
		#{
		#'new_item_text': new_item_text,
		#})



def ListPage(request):
	return render(request, 'diarylist.html')
	#return HttpResponse('<html><title>Eljohn List</title></html>')	
	#pass
#StartPage = None