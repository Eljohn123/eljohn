from django.shortcuts import redirect,render
from django.http import HttpResponse
from EList.models import Item, Login, Favorite, Archive
from EList.forms import DiaryForm
# Create your views here.
def HomePage(request):
	return render(request, 'home.html')
def LoginPage(request):
	return render(request, 'login.html')
def SignUpPage(request):
	return render(request, 'SignUp.html')
def DiaryItemList(request):
	return render(request, 'diaryitemlist.html')
def Archive(request):
	return render(request, 'archive.html')
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

#def view_list(request, DiaId):
#	list_ = Login.objects.get(id=DiaId)
	#items = Item.objects.filter(list=list_)
#	return render(request, 'diarylist.html', {'DiaId': list_})

#def new_list(request):
#	list_ = Login.objects.create()
#	Item.objects.create(
#		diary_name=request.POST['item_text'],
#		diary_date=request.POST['datenow'],
#		achi=request.POST['achi'],
#		entry=request.POST['entry'],
#		DiaId=list_)
#	return redirect(f'/EList/%d/' % (list_.id,))
#
#def add_item(request, DiaId):
#	list_ = Login.objects.get(id=DiaId)
#	Item.objects.create(
#		diary_name=request.POST['item_text'],
#		diary_date=request.POST['datenow'],
#		mood=request.POST['mood'],
#		achi=request.POST['achi'],
#		entry=request.POST['entry'],
#		DiaId=list_)
#	return redirect(f'/EList/%d/' % (list_.id,))


	#pass
#def ListPage(request):
	#return render(request, 'diarylist.html')
	#return HttpResponse('<html><title>Eljohn List</title></html>')	
	#pass
#StartPage = None
def index(request):
    diaries = Item.objects.all()
    context = {'diaries': diaries}
    return render(request, 'index.html', context)
 
def create(request):
    diary = Item(
		diary_name=request.POST['item_text'],
		diary_date=request.POST['datenow'],
    	mood=request.POST['mood'],
		achi=request.POST['achi'],
		entry=request.POST['entry'],
    	)
    diary.save()
    return redirect('/index')
 
def edit(request, id):
	diaries = Item.objects.get(id=id)
	context = {'diaries': diaries}
	return render(request, 'edit.html', context)

def update(request, id):
	diary = Item.objects.get(id=id)
	diary.diary_name = request.POST['item_text']
	diary.diary_date = request.POST['datenow']
	diary.mood=request.POST['mood']
	diary.achi=request.POST['achi']
	diary.entry=request.POST['entry']
	diary.save()
	return redirect('/index')
 
def delete(request, id):
    diary = Item.objects.get(id=id)
    diary.delete()
    return redirect('/index')