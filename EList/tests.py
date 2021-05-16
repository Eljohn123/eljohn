from django.urls import resolve
from django.test import TestCase
from EList.views import StartPage
#from EList.views import ListPage
from django.http import HttpRequest
from django.http import HttpResponse
from django.template.loader import render_to_string
from EList.models import Item, List
# Create your tests here.

class HomePageTest(TestCase):

	def test_same_url_starting_to_startpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, StartPage,)

	#def test_startpage_returns_correct_view(self):
		#request = HttpRequest()
		#response = StartPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html>'))
		#self.assertTrue(html.endswith('</html>'))

	#def test_start_page_returns_correct_view(self):
	#	request = HttpRequest()
	#	response = StartPage(request)
	#	expected_html = render_to_string('index.html')
	#	return HttpResponse(expected_html)
	#	self.assertEqual(response.content.decode(), expected_html)

	#def test_start_page_only_saves_items_when_necessary(self):
		#request = HttpRequest()
		#StartPage(request)
		#self. assertEqual(Item.objects.count(), 0)

	#def  test_start_page_displays_all_list_items(self):

		#Item.objects.create(text='itemey 1')
		#Item.objects.create(text='itemey 2')

		#request = HttpRequest()
		#response = StartPage(request)

		#self.assertIn('itemey 1', response.content.decode())
		#self.assertIn('itemey 2', response.content.decode())

	#def manually_render_a_template():

	#	self.assertIn('A new list item', response.content.decode())
	#	expected_html = render_to_string(
	#		'index.html',
	#		{'new_item_text':  'A new Diary Entry'}
	#		)
	#	self.assertEqual(response.content.decode(), expected_html)

class NewListTest(TestCase):

	def test_save_the_POST_request(self):
		self.client.post(
			'/EList/new',
			data={
			'item_text': 'A new Diary Entry',
			'datenow': 'Date Today',
			'mood': 'Mood Today'
			})
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.diary_name, 'A new Diary Entry')
			#request = HttpRequest()
		#request.method = 'POST'
		#request.POST['item_text'] = 'A new Diary Entry'

		#response = StartPage(request)

	def test_redirecting_after_POST(self):

		response = self.client.post(
			'/EList/new',
			data={
			'item_text': 'A new Diary Entry',
			'datenow': 'Date Today',
			'mood': 'Mood Today'
			})
		new_list = List.objects.first()
		self.assertRedirects(response, '/EList/%d/' % (new_list.id,))
		#request = HttpRequest()
		#request.method = 'POST'
		#request.POST['item_text'] = 'A new Diary Entry'

		#response = StartPage(request)

		#self.assertEqual(response.status_code, 302)
		#self.assertEqual(response['location'], '/EList/the-only-list-in-the-world/')

class ListAndItemModelsTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.diary_name = 'First diary entry'
		#first_item.diary_date = 'First diary date'
		first_item.DiaId = list_
		first_item.save()

		second_item = Item()
		second_item.diary_name = 'Second entry'
		second_item.DiaId = list_
		second_item.save()

		third_item = Item()
		third_item.diary_name = 'Third entry'
		third_item.DiaId = list_
		third_item.save()

		fourth_item = Item()
		fourth_item.diary_name = 'Fourth entry'
		fourth_item.DiaId = list_
		fourth_item.save()

		fifth_item = Item()
		fifth_item.diary_name = 'Fifth entry'
		fifth_item.DiaId = list_
		fifth_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 5)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		third_saved_item = saved_items[2]
		fourth_saved_item = saved_items[3]
		fifth_saved_item = saved_items[4]

		self.assertEqual(first_saved_item.diary_name, 'First diary entry')
		self.assertEqual(first_saved_item.DiaId, list_)
		self.assertEqual(second_saved_item.diary_name, 'Second entry')
		self.assertEqual(second_saved_item.DiaId, list_)
		self.assertEqual(third_saved_item.diary_name, 'Third entry')
		self.assertEqual(third_saved_item.DiaId, list_)
		self.assertEqual(fourth_saved_item.diary_name, 'Fourth entry')
		self.assertEqual(fourth_saved_item.DiaId, list_)
		self.assertEqual(fifth_saved_item.diary_name, 'Fifth entry')
		self.assertEqual(fifth_saved_item.DiaId, list_)

class ListViewTest(TestCase):
	def test_uses_list_template(self):

		list_ = List.objects.create()
		response = self.client.get('/EList/%d/' % (list_.id,))
		self.assertTemplateUsed(response, 'diarylist.html')

	def test_displays_only_items_for_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(diary_name='itemey 1', DiaId=correct_list)
		Item.objects.create(diary_name='itemey 2', DiaId=correct_list)
		other_list_ = List.objects.create()
		Item.objects.create(diary_name='other list item 1', DiaId=other_list_)
		Item.objects.create(diary_name='other list item 2', DiaId=other_list_)

		response = self.client.get('/EList/%d/' % (correct_list.id,))

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')
		self.assertNotContains(response, 'other list item 1')
		self.assertNotContains(response, 'other list item 2')

	def test_passes_correct_list_to_template(self):

		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get('/EList/%d/' % (correct_list.id,))
		self.assertEqual(response.context['DiaId'], correct_list)
#class DiaryListPage(TestCase):
	
	#def test_listpage_return_correct_view(self):
		#request = HttpRequest()
		#response = ListPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html>'))
		#self.assertIn('<title>Diary List</title>', html)
		#self.assertTrue(html.endswith('</html>'))
class NewItemTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		self.client.post(
			'/EList/%d/add_item' % (correct_list.id,),
			data={
			'item_text': 'A new entry for existing list',
			'datenow': 'Date Today',
			'mood': 'Mood Today'
			})
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.diary_name,
		'A new entry for existing list',
		'Date Today')
		self.assertEqual(new_item.DiaId, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		response = self.client.post(
			'/EList/%d/add_item' % (correct_list.id,),
			data={
			'item_text': 'A new entry for an list',
			'datenow': 'Date Today',
			'mood': 'Mood Today'}
			)
		self.assertRedirects(response, '/EList/%d/' % (correct_list.id,))