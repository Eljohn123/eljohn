from django.urls import resolve
from django.test import TestCase
from EList.views import StartPage
from EList.views import ListPage
from django.http import HttpRequest
from django.template.loader import render_to_string
from EList.models import Item
# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_startpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, StartPage, ListPage)

	#def test_startpage_returns_correct_view(self):
		#request = HttpRequest()
		#response = StartPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html>'))
		#self.assertTrue(html.endswith('</html>'))


	def test_start_page_returns_correct_view(self):
		request = HttpRequest()
		response = StartPage(request)
		html = response.content.decode('utf8')
		expected_html = render_to_string('index.html')
		#self.assertEqual(response.content.decode(), expected_html)

	def test_start_page_can_save_a_POST_request(self):

		request = HttpRequest()
		
		request.method = 'POST'
		
		request.POST['item_text'] = 'A new list item'

		response = StartPage(request)
		html = response.content.decode('utf8')

	def manually_render_a_template():

		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'index.html',
			{'new_item_text':  'A new list item'}
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


#class DiaryListPage(TestCase):
	
	#def test_listpage_return_correct_view(self):
		#request = HttpRequest()
		#response = ListPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html>'))
		#self.assertIn('<title>Diary List</title>', html)
		#self.assertTrue(html.endswith('</html>'))