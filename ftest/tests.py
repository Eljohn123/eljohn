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
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('Cloud Diary', self.browser.title)
		#self.fail('Finish the test Now!!!????')
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('diarylist')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

		#inputbox.send_keys(Keys.ENTER)
		#self.check_for_row_in_list_table('1: Diary Entry')

		#inputbox = self.browser.find_element_by_id('saveinput')
		#inputbox.send_keys('DateToday')
		#inputbox.send_keys(Keys.ENTER)

		#self.check_for_row_in_list_table('1: Diary Entry')
		#self.check_for_row_in_list_table('2: DateToday')
	#def test_layout_and_styling(self):
		
	#	self.browser.get(self.live_server_url)
	#	self.browser.set_window_size(1024, 768)

	#	inputbox = self.browser.find_element_by_id('saveinput')
	#	inputbox.send_keys('testing\n')
	#	self.assertAlmostEqual(
	#		inputbox.location['x'] + inputbox.size['width'] / 2, 512,
	#		delta=5
	#	)

	def test_start_list_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Cloud Diary', self.browser.title)

		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Cloud Diary', headerText)

		#headerText = self.browser.find_element_by_tag_name('h4').text
		#self.assertIn('Date', headerText)

		headerText = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('Diary', headerText)

		inputdatebox = self.browser.find_element_by_id('currentDate')
		self.assertEqual(inputdatebox.get_attribute('placeholder'), 'Date Today')
		inputdatebox.send_keys('4/30/2021')
		time.sleep(1)


		mood = self.browser.find_element_by_id('mood')
		self.assertEqual(mood.get_attribute('placeholder'), 'Your mood?')
		mood.send_keys('Happy')
		time.sleep(1)


		achieve = self.browser.find_element_by_id('achieve')
		self.assertEqual(achieve.get_attribute('placeholder'), 'Achievements Today')
		achieve.send_keys('Written a poem')
		time.sleep(1)


		entry = self.browser.find_element_by_id('entry')
		self.assertEqual(entry.get_attribute('placeholder'), 'Your Entry')
		entry.send_keys('Today I did something awesome!')
		time.sleep(1)

		inputbox = self.browser.find_element_by_id('saveinput')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Diary Name')
		inputbox.send_keys('Diary Entry')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		eljohn_list_url = self.browser.current_url
		self.assertRegex(eljohn_list_url, '/EList/.+')
		self.check_for_row_in_list_table('1: Diary Entry')
		
		inputdatebox = self.browser.find_element_by_id('currentDate')
		self.assertEqual(inputdatebox.get_attribute('placeholder'), 'Date Today')
		inputdatebox.send_keys('5/5/2021')
		time.sleep(1)

		mood = self.browser.find_element_by_id('mood')
		self.assertEqual(mood.get_attribute('placeholder'), 'Your mood?')
		mood.send_keys('Sad')
		time.sleep(1)


		achieve = self.browser.find_element_by_id('achieve')
		self.assertEqual(achieve.get_attribute('placeholder'), 'Achievements Today')
		achieve.send_keys('My pet died')
		time.sleep(1)


		entry = self.browser.find_element_by_id('entry')
		self.assertEqual(entry.get_attribute('placeholder'), 'Your Entry')
		entry.send_keys('Today is a very sad day.')
		time.sleep(1)


		inputbox = self.browser.find_element_by_id('saveinput')
		inputbox.send_keys('Diary Entry 2')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		#self.fail('Finish the Test!')
		
		self.check_for_row_in_list_table('2: Diary Entry 2')
		self.check_for_row_in_list_table('1: Diary Entry')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Diary Entry', page_text)
		self.assertNotIn('Date Today', page_text)

		inputdatebox = self.browser.find_element_by_id('currentDate')
		self.assertEqual(inputdatebox.get_attribute('placeholder'), 'Date Today')
		inputdatebox.send_keys('5/10/2021')
		time.sleep(1)

		mood = self.browser.find_element_by_id('mood')
		self.assertEqual(mood.get_attribute('placeholder'), 'Your mood?')
		mood.send_keys('Energetic')
		time.sleep(1)


		achieve = self.browser.find_element_by_id('achieve')
		self.assertEqual(achieve.get_attribute('placeholder'), 'Achievements Today')
		achieve.send_keys('Written a many names.')
		time.sleep(1)

		entry = self.browser.find_element_by_id('entry')
		self.assertEqual(entry.get_attribute('placeholder'), 'Your Entry')
		entry.send_keys('Today I wrote many names of many different people')
		time.sleep(1)


		inputbox = self.browser.find_element_by_id('saveinput')
		inputbox.send_keys('Death Note Diary #1')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		
		inputdatebox = self.browser.find_element_by_id('currentDate')
		self.assertEqual(inputdatebox.get_attribute('placeholder'), 'Date Today')
		inputdatebox.send_keys('5/12/2021')
		time.sleep(1)


		mood = self.browser.find_element_by_id('mood')
		self.assertEqual(mood.get_attribute('placeholder'), 'Your mood?')
		mood.send_keys('Cool')
		time.sleep(1)


		achieve = self.browser.find_element_by_id('achieve')
		self.assertEqual(achieve.get_attribute('placeholder'), 'Achievements Today')
		achieve.send_keys('Solved a very hard puzzle.')
		time.sleep(1)


		entry = self.browser.find_element_by_id('entry')
		self.assertEqual(entry.get_attribute('placeholder'), 'Your Entry')
		entry.send_keys('Today I solved the hardest puzzle ever.')
		time.sleep(1)


		inputbox = self.browser.find_element_by_id('saveinput')
		inputbox.send_keys('Death Note Diary #2')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		newuser_list_url = self.browser.current_url
		self.assertRegex(newuser_list_url, '/EList/.+')
		self.assertNotEqual(newuser_list_url, eljohn_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Diary Entry', page_text)
		self.assertIn('Death Note Diary #1', page_text)


		#script = self.browser.find_element_by_id('scriptdate')
		#self.assertEqual(script.get_attribute('placeholder'), 'DateToday')
		
		#table = self.browser.find_element_by_id('diarylist')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn('1: Diary Entry', [row.text for row in rows]),
		#"New to-do item did not appear in table -- its text was:\n%s" % (table.text,)
		#self.assertIn('2: DateToday' ,[row.text for row in rows])
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
