import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_SS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_Successful_Search(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://team2tvs.herokuapp.com/")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="search-form"]/form/input')
       elem.send_keys("smart")
       elem = driver.find_element_by_xpath('//*[@id="search-form"]/form/input[2]').click()
       time.sleep(4)

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()
