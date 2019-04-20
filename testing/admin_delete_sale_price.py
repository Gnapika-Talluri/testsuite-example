import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_ADSP(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_delete_sale_price(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://team2tvs.herokuapp.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[2]/th/a').click()
        time.sleep(1)
        blank = driver.find_element_by_id("id_form-2-price")
        blank.clear()
        time.sleep(1)
        driver.find_element_by_id("id_form-2-price").send_keys("44.50")
        time.sleep(1)
        blank = driver.find_element_by_id("id_form-2-regular_price")
        blank.clear()
        driver.find_element_by_xpath('//*[@id="changelist-form"]/p/input').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()