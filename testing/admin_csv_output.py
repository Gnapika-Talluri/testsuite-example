import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Cart_CSV(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_CSV(self):
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
        time.sleep(4)
        # Select 'Export to CSV' option
        driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/label/select').click()
        driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/label/select/option[3]').click()
        time.sleep(4)
        # Select one order
        #driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[1]/input').click()
        # Click 'Go'
        #driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/button').click()
        #time.sleep(2)

        # Select multiple orders
        #driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[2]/td[1]/input').click()
        #driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[3]/td[1]/input').click()
        #driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[4]/td[1]/input').click()

        driver.find_element_by_xpath('// *[ @ id = "action-toggle"]').click()
        # Click 'Go'
        driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/button').click()
        time.sleep(7)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()