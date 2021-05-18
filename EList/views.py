from django.shortcuts import redirect,render
from django.http import HttpResponse
from EList.models import Item, List
# Create your views here.
def StartPage(request):
	return render(request, 'index.html')
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
	
		#{
		#'new_item_text': new_item_text,
		#})

def view_list(request, DiaId):
	list_ = List.objects.get(id=DiaId)
	#items = Item.objects.filter(list=list_)
	return render(request, 'diarylist.html', {'DiaId': list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(
		diary_name=request.POST['item_text'],
		diary_date=request.POST['datenow'],
		mood=request.POST['mood'],
		achi=request.POST['achi'],
		entry=request.POST['entry'],
		DiaId=list_)
	return redirect(f'/EList/%d/' % (list_.id,))

def add_item(request, DiaId):
	list_ = List.objects.get(id=DiaId)
	Item.objects.create(
		diary_name=request.POST['item_text'],
		diary_date=request.POST['datenow'],
		mood=request.POST['mood'],
		achi=request.POST['achi'],
		entry=request.POST['entry'],
		DiaId=list_)
	return redirect(f'/EList/%d/' % (list_.id,))
	#pass
#def ListPage(request):
	#return render(request, 'diarylist.html')
	#return HttpResponse('<html><title>Eljohn List</title></html>')	
	#pass
#StartPage = None