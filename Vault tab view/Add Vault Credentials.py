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


    def test_Add_Vault_Credentials(self):
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


        #Add Vault credentials modal
        self.addusercredentials = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/vault-credentials-list-component/app-master-view/div[1]/div[2]/config-button-component/div/button')
        self.addusercredentials.click()
        time.sleep(2)
        self.driver.implicitly_wait(2)

        #Vault credentials name
        self.tickcredentialname = self.driver.find_element_by_xpath('//*[@id="inputCredentialName"]')
        credentialname = 'Automated creds' .join(random.choice(string.ascii_lowercase) for _ in range(2))
        self.tickcredentialname.send_keys(credentialname)
        time.sleep(2)
        self.driver.implicitly_wait(2)

        #HostnameURL
        self.hostnameurl = self.driver.find_element_by_xpath('//*[@id="inputDescription"]')
        hostnameurl = 'test.id.overwatchid.com'
        self.hostnameurl.send_keys(hostnameurl)
        time.sleep(1)
        self.driver.implicitly_wait(2)

        #Click Authentication
        """
        self.authenticationclick = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-vault-credentials-modal/div/div/div/div[2]/tabset/div/tab/div[3]/div/accordion/accordion-group[1]/div/div[1]')
        self.authenticationclick.click()
        time.sleep(1)
        self.driver.implicitly_wait(1)"""

        #Fill in UserName
        self.vaultusername = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-vault-credentials-modal/div/div/div/div[2]/tabset/div/tab/div[3]/div/accordion/accordion-group[1]/div/div[2]/div/authentication/div/div[1]/div/input')
        vaultusername = 'username'.join(random.choice(string.ascii_lowercase)for _ in range (2))
        self.vaultusername.send_keys(vaultusername)
        time.sleep(1)
        self.driver.implicitly_wait(1)

        #fill in Password
        self.vaultpassword = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-vault-credentials-modal/div/div/div/div[2]/tabset/div/tab/div[3]/div/accordion/accordion-group[1]/div/div[2]/div/authentication/div/div[2]/div/password-form/div/input')
        vaultpassword = 'R0cknit!'
        self.vaultpassword.send_keys(vaultpassword)
        time.sleep(1)
        self.driver.implicitly_wait(1)

        #Save vault credentials
        self.savevault = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-vault-credentials-modal/div/div/div/div[2]/tabset/div/tab/div[4]/div/div/button[1]')
        self.savevault.click()



if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
