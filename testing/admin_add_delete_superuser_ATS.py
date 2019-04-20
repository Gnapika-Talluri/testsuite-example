import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Admin_ADSU(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addmin_add_delete_superuser(self):

        # login 'instructor'
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://team2tvs.herokuapp.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "'instructor' Logged In"
        time.sleep(3)

        # add new user
        driver.get("http://team2tvs.herokuapp.com/admin/auth/user/add")
        time.sleep(3)
        user = "new_superuser"
        pwd = "ATS-pass1"
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys(pwd)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "New User Added"
        time.sleep(3)

        # add email & permissions
        email = 'new@superuser.com'
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        time.sleep(2)
        driver.find_element_by_id("id_is_staff").click()
        time.sleep(2)
        driver.find_element_by_id("id_is_superuser").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        assert "New User Email & Permissions Added"
        time.sleep(3)

        # logout 'instructor', login new user, logout new user
        driver.get("http://team2tvs.herokuapp.com/admin/logout/")
        time.sleep(3)
        assert "'instructor' Logged Out"
        driver.get("http://team2tvs.herokuapp.com/admin")
        time.sleep(2)
        user = "new_superuser"
        pwd = "ATS-pass1"
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "New User Logged In"
        time.sleep(5)
        driver.get("http://team2tvs.herokuapp.com/admin/logout/")
        assert "New User Logged Out"
        time.sleep(3)

        # login 'instructor', delete new user
        user = "instructor"
        pwd = "instructor1a"
        driver.get("http://team2tvs.herokuapp.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "'instructor' Logged In"
        time.sleep(3)
        driver.get("http://team2tvs.herokuapp.com/admin/auth/user")
        time.sleep(3)
        driver.find_element_by_xpath("//*[contains(text(), 'new_superuser')]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        assert "New User Deleted"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
