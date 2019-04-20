import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Cart_AI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # add new televison
    def test_add_item(self):
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
        driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[2]/td[1]/a').click()
        s1 = Select(driver.find_element_by_id('id_category'))
        s1.select_by_index(1)
        driver.find_element_by_id("id_name").send_keys("Samsung LED TV 55 in. | Model TV1234")
        driver.find_element_by_id("id_slug").send_keys("")
        #driver.find_element_by_xpath('//*[@id="id_image"]').send_keys('/Users/bodaj/Downloads/no_image.png')
        driver.find_element_by_id("id_price").send_keys("399.99")
        driver.find_element_by_id("id_tv_size").send_keys("55")
        driver.find_element_by_id("id_description").send_keys("This is a description. This is a description. This is a description.")
        driver.find_element_by_xpath('//*[@id="product_form"]/div/div/input[1]').click()

        # add accessory (is_streaming)
        driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
        s1 = Select(driver.find_element_by_id('id_category'))
        s1.select_by_index(2)
        driver.find_element_by_id("id_name").send_keys("Sony Accessory (streaming)")
        driver.find_element_by_id("id_slug").send_keys("")
        #driver.find_element_by_xpath('//*[@id="id_image"]').send_keys('/Users/bodaj/Downloads/no_image.png')
        driver.find_element_by_id("id_price").send_keys("99.99")
        driver.find_element_by_xpath('//*[@id="id_is_streaming"]').click()
        driver.find_element_by_id("id_description").send_keys("This is a description. This is a description. This is a description.")
        driver.find_element_by_xpath('//*[@id="product_form"]/div/div/input[3]').click()
        blank = driver.find_element_by_id("id_description")
        blank.clear()
        driver.find_element_by_id("id_description").send_keys("This description has been edited.")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="product_form"]/div/div/input[1]').click()
        driver.get("https://team2tvs.herokuapp.com/admin")

        # add accessory (is_cable)
        driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[2]/td[1]/a').click()
        s1 = Select(driver.find_element_by_id('id_category'))
        s1.select_by_index(2)
        driver.find_element_by_id("id_name").send_keys("LG Accessory (cable)")
        driver.find_element_by_id("id_slug").send_keys("")
        #driver.find_element_by_xpath('//*[@id="id_image"]').send_keys('/Users/bodaj/Downloads/no_image.png')
        driver.find_element_by_id("id_price").send_keys("79.99")
        driver.find_element_by_xpath('//*[@id="id_is_cable"]').click()
        driver.find_element_by_id("id_description").send_keys("This is a description. This is a description. This is a description.")
        driver.find_element_by_xpath('//*[@id="product_form"]/div/div/input[1]').click()
        driver.get("https://team2tvs.herokuapp.com/admin")

        # add accessory (tv care)
        driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[2]/td[1]/a').click()
        s1 = Select(driver.find_element_by_id('id_category'))
        s1.select_by_index(2)
        driver.find_element_by_id("id_name").send_keys("Vizio Accessory (tv care)")
        driver.find_element_by_id("id_slug").send_keys("")
        #driver.find_element_by_xpath('//*[@id="id_image"]').send_keys('/Users/bodaj/Downloads/no_image.png')
        driver.find_element_by_id("id_price").send_keys("49.99")
        driver.find_element_by_xpath('//*[@id="id_is_tv_care"]').click()
        driver.find_element_by_id("id_description").send_keys("This is a description. This is a description. This is a description.")
        driver.find_element_by_xpath('//*[@id="product_form"]/div/div/input[1]').click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()