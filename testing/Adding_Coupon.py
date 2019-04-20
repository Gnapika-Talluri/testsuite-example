import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_AC(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_adding_coupon(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://team2tvs.herokuapp.com/admin")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("instructor")
       elem = driver.find_element_by_id("id_password")
       elem.send_keys("instructor1a")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr/th/a').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_code")
       elem.send_keys("testcode")
       time.sleep(3)
       elem = driver.find_element_by_xpath('//*[@id="coupon_form"]/div/fieldset/div[2]/div/p/span[1]/a[1]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="coupon_form"]/div/fieldset/div[2]/div/p/span[2]/a[1]').click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_valid_to_0")
       elem.send_keys("2019-05-21")
       elem = driver.find_element_by_id("id_valid_to_1")
       elem.send_keys("12:00:00")
       time.sleep(2)
       elem = driver.find_element_by_id("id_discount")
       elem.send_keys("15")
       elem = driver.find_element_by_xpath('//*[@id="id_active"]').click()
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="coupon_form"]/div/div/input[1]').click()
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()