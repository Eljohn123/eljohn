from django.urls import resolve
from django.test import TestCase
from EList.views import StartPage
from django.http import HttpRequest
# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_startpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, StartPage)

	def test_startpage_returns_correct_view(self):
		request = HttpRequest()
		response = StartPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>Eljohn List</title>', html)
		self.assertTrue(html.endswith('</html>'))