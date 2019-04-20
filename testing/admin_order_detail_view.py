import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Cart_AODV(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_AdminOrderDetailView(self):
        driver = self.driver
        driver.maximize_window()
        user = "instructor"
        pwd = "instructor1a"
        driver.get("https://team2tvs.herokuapp.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        # Open order page
        driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr/th/a').click()
        time.sleep(3)
        # Open order view page
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[12]/a').click()
        time.sleep(7)

        # Go back to home page and do process again with a different order
        #driver.find_element_by_xpath('//*[@id="container"]/div[2]/a[1]').click()
        # Open order page
        #driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr/th/a').click()
        #time.sleep(1)
        # Open order view page
        #driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[5]/td[12]/a').click()
        #time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()