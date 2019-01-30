import datetime
import time
import string
import random
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Full_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #create a new chrome test session
        #set the webdriver exec path
        self.driver = webdriver.Chrome(executable_path='C:/Users/kenma/Downloads/chromedriver_win/chromedriver')
        self.driver.implicitly_wait(2)

        #navigate the web address
        self.driver.get("https://test.id.overwatchid.com/login")
        self.driver.implicitly_wait(2)

        self.driver.maximize_window()


    def test_1a_Vault_tab_view(self):
        #valid username
        self.driver.implicitly_wait(2)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.send_keys("narman@test.com")
        self.driver.implicitly_wait(2)
        self.loginbtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/input')
        self.loginbtn.click()
        self.driver.implicitly_wait(2)
        time.sleep(5)
        #valid Password
        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.send_keys("R0cknit!")
        #Login
        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        self.driver.implicitly_wait(2)
        time.sleep(4)

        #Navigate to Vault tab
        self.tickVault = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[2]/div[2]/ul/li[2]/a')
        self.tickVault.click()

        time.sleep(3)
        self.driver.implicitly_wait(3)
        #Assert vault credentials main view
        self.vaultcredentialview = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/vault-credentials-list-component/app-master-view/div[1]/div[1]/h3')
        assert self.vaultcredentialview.text == 'Vault Credentials'
        if self.vaultcredentialview.text == u'Vault Credentials':
            print ("Vault Credentials Main view Verified:")


if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
