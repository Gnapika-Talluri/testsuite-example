import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Cart_DOFC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_order_from_cart(self):
        driver = self.driver
        driver.maximize_window()

        # add 1 item to cart and remove it
        driver.get("https://team2tvs.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td[4]/a').click()
        time.sleep(2)

        #add 2 items to cart and remove 1
        driver.get("https://team2tvs.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        driver.get("https://team2tvs.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td[4]/a').click()
        time.sleep(2)

        #add 2 items to cart and remove both
        driver.get("https://team2tvs.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        driver.get("https://team2tvs.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td[4]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td[4]/a').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()