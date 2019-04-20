import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_PO(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_place_order(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://team2tvs.herokuapp.com/")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="pagination"]/div/div/nav/ul/li[3]/a').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="id_quantity"]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content"]/div[2]/a[2]').click()
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Test")
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Name")
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("patrickfaughn@gmail.com")
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("123 test st.")
       elem = driver.find_element_by_id("id_postal_code")
       elem.send_keys("68114")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("NE")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content"]/form/p[7]/input').click()
       time.sleep(2)



   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()