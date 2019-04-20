import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_SB(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_sort_by(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://team2tvs.herokuapp.com/")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="pagination"]/div/div/nav/ul/li[3]/a').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div[1]/a[1]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div[1]/a[2]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div[1]/a[3]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[3]/a').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div[2]/a[1]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div[2]/a[2]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="sidebar"]/ul/div[2]/a[3]').click()
       time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()