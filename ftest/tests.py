from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	#def test_browser_title(self):
		#self.browser.get('http://localhost:8000')
		#self.assertIn('Eljohn List', self.browser.title)
		#self.fail('Finish the test Now!!!????')
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('diarylist')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for now in rows])

		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Diary Entry')

		inputbox = self.browser.find_element_by_id('saveinput')
		inputbox.send_keys('DateToday')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: Diary Entry')
		self.check_for_row_in_list_table('2: DateToday')

	def test_start_list_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Cloud Diary', self.browser.title)

		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Cloud Diary', headerText)

		headerText = self.browser.find_element_by_tag_name('h4').text
		self.assertIn('Date', headerText)

		headerText = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('Diary', headerText)

		inputbox = self.browser.find_element_by_id('saveinput')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'What happened today..')
		inputbox.send_keys('Diary Entry')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(3)

		inputbox = self.browser.find_element_by_id('saveinput')
		inputbox.send_keys('DateToday')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(3)

		#self.fail('Finish the Test!')

		#script = self.browser.find_element_by_id('scriptdate')
		#self.assertEqual(script.get_attribute('placeholder'), 'DateToday')
		
		table = self.browser.find_element_by_id('diarylist')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Diary Entry', [row.text for row in rows]),
		"New to-do item did not appear in table -- its text was:\n%s" % (table.text,)
		self.assertIn('2: DateToday' ,[row.text for row in rows])
		#self.fail('Finish the test')


#class DiaryPageTest(unittest.TestCase):

	#def setUp(self):
	#	self.browser = webdriver.Firefox()
	#	self.browser.implicitly_wait(3)

	#def tearDown(self):
	#	self.browser.quit()

				
	#def test_diary_list_retrieve_it(self):
	#	self.browser.get('http://localhost:8800')
	#	self.assertIn('Diary List', self.browser.title)

#if __name__== '__main__':
#	unittest.main(warnings = 'ignore')
