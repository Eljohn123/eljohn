from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	#def test_browser_title(self):
		#self.browser.get('http://localhost:8000')
		#self.assertIn('Eljohn List', self.browser.title)
		#self.fail('Finish the test Now!!!????')

	def test_start_list_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Cloud Diary', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Cloud Diary', headerText)
		headerText = self.browser.find_element_by_tag_name('h4').text
		self.assertIn('Date', headerText)
		textarea = self.browser.find_element_by_tag_name('textarea').text
		#inputbox = self.browser.find_element_by_id('today')
		#self.assertEqual(inputbox.get_attribute('placeholder'), 'Write your experiences today')
		#inputbox.send_keys('Today I did something awesome.')
		#inputbox.send_keys(Keys.ENTER)
		#time.sleep(2)
		saveinput = self.browser.find_element_by_id('saveinput')
		#inputbox.send_keys('Today I did something awesome.')
		#inputbox.send_keys(Keys.ENTER)
		self.assertEqual(saveinput.get_attribute('placeholder'), 'What happened today..')
		#dateinput = self.browser.find_element_by_id('dateinput')
		#self.assertEqual(dateinput.get_attribute('placeholder'), 'Date Today')
		#headerText = self.browser.find_element_by_tag_name('h5').text
		#self.assertIn('Date', headerText)
		headerText = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('Diary', headerText)

		#table = self.browser.find_element_by_id('idListTable')
		#rows = table.find_element_by_tag_name('tr')
		#self.assertTrue(any(row.text == '1: Eljohn Torres'))
		#self.fail('Finish the test')

if __name__== '__main__':
	unittest.main(warnings = 'ignore')
