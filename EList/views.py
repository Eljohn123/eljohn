from django.shortcuts import redirect,render
from django.http import HttpResponse
from EList.models import Item, List
# Create your views here.
def StartPage(request):
	#item = Item()
	#item.text = request.POST.get('item_text', '')
	#item.save()
	#if request.method == 'POST':
	#	Item.objects.create(text=request.POST['item_text'])
	#	return redirect('/EList/the-only-list-in-the-world/')
		#new_item_text = request.POST['item_text']
		#Item.objects.create(text=new_item_text)
	#else:
		#new_item_text = ''
	#items = Item.objects.all()
	return render(request, 'index.html')
		#{
		#'new_item_text': new_item_text,
		#})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	#items = Item.objects.filter(list=list_)
	return render(request, 'diarylist.html', {'list': list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/EList/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/EList/%d/' % (list_.id,))

	#pass
#def ListPage(request):
	#return render(request, 'diarylist.html')
	#return HttpResponse('<html><title>Eljohn List</title></html>')	
	#pass
#StartPage = None