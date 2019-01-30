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


    def test_1a_View_Challenge_Questions(self):
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
        self.testlogin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/connections-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.testlogin.text == 'Search All Connections'
        if self.testlogin.text == u'Search All Connections':
            print ("Valid login Verified")

        #Go to admin tab
        self.driver.implicitly_wait(2)
        self.admintab  = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[2]/div[2]/ul/li[4]/a')
        self.driver.implicitly_wait(2)
        self.admintab.click()
        self.driver.implicitly_wait(2)

        self.testadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.driver.implicitly_wait(2)
        assert self.testadmin.text == 'Account Administration'
        if self.testadmin.text == u'Account Administration':
            print "Admin tab verified"
        #Go to Account Administration
        self.driver.implicitly_wait(2)
        self.accntadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/tree-node-expander/span')
        self.driver.implicitly_wait(2)
        self.accntadmin.click()

        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.tocq = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.tocq.click()
        #Verify if the challenge questions main view loaded successfully
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.vercqview = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[1]/div/h4')
        assert self.vercqview.text == 'Challenge Questions'
        if self.vercqview.text == u'Challenge Questions':
            print "Challenge Questions Main View Verified"

        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.tickAddChallQuestions = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[2]/div/div[1]/div[1]/div/i')
        self.tickAddChallQuestions.click()

        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.addcqmodal = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[1]/h4')
        assert self.addcqmodal.text == 'Add Question'
        if self.addcqmodal.text == u'Add Question':
            print "Add Question Modal is Present"

        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.tickAddChallengeQuestionsTextbox = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[2]/tabset/div/tab/div[1]/div/div/input')
        self.tickAddChallengeQuestionsTextbox.click()

        self.driver.implicitly_wait(2)
        time.sleep(2)
        ChallengeQuestion = 'Can you decode it?'.join(random.choice(string.ascii_uppercase) for _ in range (2))
        self.tickAddChallengeQuestionsTextbox.send_keys(ChallengeQuestion)

        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.tickaddcq = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[2]/tabset/div/tab/div[2]/div/div/button[1]')
        self.tickaddcq.click()

        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.savecq =  self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[2]/div/div[2]/div/div/button')
        self.savecq.click()
        self.driver.implicitly_wait(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
