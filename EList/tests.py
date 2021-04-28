from django.urls import resolve
from django.test import TestCase
from EList.views import StartPage
#from EList.views import ListPage
from django.http import HttpRequest
from django.http import HttpResponse
from django.template.loader import render_to_string
from EList.models import Item
# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_startpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, StartPage,)

	#def test_startpage_returns_correct_view(self):
		#request = HttpRequest()
		#response = StartPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html>'))
		#self.assertTrue(html.endswith('</html>'))

	def test_start_page_returns_correct_view(self):
		request = HttpRequest()
		response = StartPage(request)
		expected_html = render_to_string('index.html')
		return HttpResponse(expected_html)
		self.assertEqual(response.content.decode(), expected_html)
		

	def test_start_page_can_save_a_POST_request(self):

		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new Diary Entry'

		response = StartPage(request)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new Diary Entry')

	def test_start_page_redirects_after_POST(self):

		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new Diary Entry'

		response = StartPage(request)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/EList/the-only-list-in-the-world/')

	def test_start_page_only_saves_items_when_necessary(self):
		request = HttpRequest()
		StartPage(request)
		self. assertEqual(Item.objects.count(), 0)

	#def  test_start_page_displays_all_list_items(self):

		#Item.objects.create(text='itemey 1')
		#Item.objects.create(text='itemey 2')

		#request = HttpRequest()
		#response = StartPage(request)

		#self.assertIn('itemey 1', response.content.decode())
		#self.assertIn('itemey 2', response.content.decode())

	def manually_render_a_template():

		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'index.html',
			{'new_item_text':  'A new Diary Entry'}
			)
		self.assertEqual(response.content.decode(), expected_html)

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'First diary entry'
		first_item.save()

		second_item = Item()
		second_item.text = 'Second entry'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'First diary entry')
		self.assertEqual(second_saved_item.text, 'Second entry')

class ListViewTest(TestCase):
	def test_uses_list_template(self):

		response = self.client.get('/EList/the-only-list-in-the-world/')
		self.assertTemplateUsed(response, 'diarylist.html')

	def test_displays_all_items(self):

		Item.objects.create(text='itemey 1')
		Item.objects.create(text='itemey 2')

		response = self.client.get('/EList/the-only-list-in-the-world/')

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')
#class DiaryListPage(TestCase):
	
	#def test_listpage_return_correct_view(self):
		#request = HttpRequest()
		#response = ListPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html>'))
		#self.assertIn('<title>Diary List</title>', html)
		#self.assertTrue(html.endswith('</html>'))