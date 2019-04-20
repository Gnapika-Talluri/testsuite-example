import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_SP(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_successful_payment(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://team2tvs.herokuapp.com/")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="pagination"]/div/div/nav/ul/li[4]/a').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="id_quantity"]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content"]/div[2]/a[2]').click()
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("George")
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Royce")
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("groyce@unomaha.edu.com")
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("4010 address")
       elem = driver.find_element_by_id("id_postal_code")
       elem.send_keys("68105")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("NE")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content"]/form/p[8]/input').click()
       time.sleep(27)


       time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
