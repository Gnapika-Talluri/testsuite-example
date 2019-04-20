import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Cart_ADI(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_delete_item(self):
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

        # sort by date created
        driver.find_element_by_xpath('//*[@id="result_list"]/thead/tr/th[7]/div[1]/a').click()
        driver.find_element_by_xpath('//*[@id="result_list"]/thead/tr/th[7]/div[2]/a').click()
        time.sleep(1)

        # select all, then unselect all
        driver.find_element_by_xpath('// *[ @ id = "action-toggle"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('// *[ @ id = "action-toggle"]').click()
        time.sleep(1)
        # delete multiple
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[1]/input').click()
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[3]/td[1]/input').click()
        # select 4th item and then deselect it
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[4]/td[1]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[4]/td[1]/input').click()
        time.sleep(1)
        s1 = Select(driver.find_element_by_xpath('//*[@id="changelist-form"]/div[2]/label/select'))
        s1.select_by_index(1)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="changelist-form"]/div[2]/button').click()
        # select, no
        driver.find_element_by_xpath('//*[@id="content"]/form/div/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="changelist-form"]/div[2]/button').click()
        # select yes
        driver.find_element_by_xpath('//*[@id="content"]/form/div/input[6]').click()

        # delete 1
        driver.get("https://team2tvs.herokuapp.com/admin")
        driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/table/tbody/tr[2]/th/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="result_list"]/thead/tr/th[7]/div[1]/a').click()
        driver.find_element_by_xpath('//*[@id="result_list"]/thead/tr/th[7]/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[1]/input').click()
        time.sleep(1)
        s1 = Select(driver.find_element_by_xpath('//*[@id="changelist-form"]/div[2]/label/select'))
        s1.select_by_index(1)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="changelist-form"]/div[2]/button').click()
        # select yes
        driver.find_element_by_xpath('//*[@id="content"]/form/div/input[4]').click()
        time.sleep(2)

    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()