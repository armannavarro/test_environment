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
        time.sleep(1)

    def test_1a_Log_in_with_Invalid_Credentials(self):
        #Invalid username
        time.sleep(3)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.send_keys("gentss@test.com")
        time.sleep(2)
        self.loginbtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/input')
        self.loginbtn.click()
        time.sleep(1)
        #Invalid Password
        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.send_keys("Invalid")
        #Login
        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        time.sleep(1)
        self.invalidmessage = self.driver.find_element_by_tag_name('p')
        assert self.invalidmessage.text == 'Your login attempt was not successful.'
        if self.invalidmessage.text == u'Your login attempt was not successful.':
            print "Verify invalid login:"

    def test_1b_Log_in_with_Valid_Credentials(self):
        time.sleep(1)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.clear()
        self.user_name.send_keys("release@test.com")
        time.sleep(1)

        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.clear()
        self.password.send_keys("R0cknit!")

        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        time.sleep(1)
        self.testlogin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/connections-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.testlogin.text == 'Search All Connections'
        if self.testlogin.text == u'Search All Connections':
            print "Verify valid login:"


    def test_2a_Admin(self):
        #Go to admin tab
        time.sleep(3)
        self.admintab  = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[2]/div[2]/ul/li[4]/a')
        time.sleep(1)
        self.admintab.click()
        time.sleep(2)

        self.testadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span')
        time.sleep(3)
        assert self.testadmin.text == 'Account Administration'
        if self.testadmin.text == u'Account Administration':
            print "Admin Tab Present:"


    def test_2b_Account_Administration(self):
        #Go to Account Administration
        time.sleep(3)
        self.accntadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/tree-node-expander/span')
        time.sleep(1)
        self.accntadmin.click()
        time.sleep(1)
        #Go to API Keys
        self.api = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.api.click()
        time.sleep(1)
        #Add api key button
        self.addapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/tapik-component/app-master-view/div[1]/div[2]/config-button-component/div/button')
        self.addapi.click()
        time.sleep(2)

        #Assert if Add API Modal is present
        self.addapimodal = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[1]/h4')
        assert self.addapimodal.text == 'Add API Key'
        if self.addapimodal.text == u'Add API Key':
            print "Add API Modal is Present:"

    def test_2c_Add_API_KEY_with_default_Expiration(self):
        #add api
        time.sleep(2)
        self.apiname = self.driver.find_element_by_xpath('//*[@id="inputName"]')
        apiname = 'Automated Test '.join(random.choice(string.ascii_lowercase) for _ in range (2))
        self.apiname.send_keys(apiname) #api name
        time.sleep(0.5)
        self.desapi = self.driver.find_element_by_xpath('//*[@id="inputDescription"]')
        des = 'Description'
        self.desapi.send_keys(des) #api description
        time.sleep(0.5)
        self.apiemail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        apiemail = 'arman.navarro@teravibe.com'
        self.apiemail.send_keys(apiemail) #api email

        #select Role
        try:
            time.sleep(3)
            self.apirole = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[2]/app-master-dropdown/form/div/ng-select/div/div')
            if self.apirole.is_element_present():
                self.apirole.click()
        except NoSuchElementException:
            print('Element api role xpath not found')
            time.sleep(3)
            self.clickout1 = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div')
            self.clickout1.click()

        time.sleep(3)
        try:
            self.pickrole = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[2]/app-master-dropdown/form/div/ng-select/select-dropdown/div/div/ul/li[1]')
            if self.pickrole.is_element_present():
                self.apirole.click()
        except NoSuchElementException:
            print('Element api role xpath not found')
            time.sleep(2)
            self.clickout2 = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div')
            self.clickout2.click()
        time.sleep(1)
        #select user groups
        self.apigroup = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[3]/app-master-dropdown/form/div/ng-select/div/div/input')
        self.apigroup.click()
        time.sleep(1)
        self.picgroup = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[3]/app-master-dropdown/form/div/ng-select/select-dropdown/div/div/ul/li[3]')
        self.picgroup.click()
        #save_api
        time.sleep(1)
        self.saveapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[4]/div/confirm-cancel-component/div/button[1]')
        self.saveapi.click()
        time.sleep(3)

    def test_2d_Verify_Add_API_Success(self):
        try:
            self.apisuccess = self.driver.find_element_by_xpath('/div/nac-alert/div')
            time.sleep(3)
            assert self.apisuccess.text == 'Creation Success! Entity was successfully created'
            if self.addapimodal.text == u'Creation Success! Entity was successfully created':
                print ("Verify API Key was added:")
        except NoSuchElementException:
                print ("Unable to retrieve success message")

    def test_3d_Challenge_Questions(self):
        #Assert if challenge question is present
        time.sleep(3)
        self.vercq = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.vercq.text == 'Challenge Questions'
        if self.vercq.text == u'Challenge Questions':
            print "Verify Challenge Questions is Present from the tree:"

    def test_4d_Navigate_Challenge_Questions(self):
        #navigate to challenge questions
        self.tocq = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.tocq.click()
        #Verify if the challenge questions main view loaded successfully
        time.sleep(2)
        self.vercqview = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[1]/div/h4')
        assert self.vercqview.text == 'Challenge Questions'
        if self.vercqview.text == u'Challenge Questions':
            print "Verify Challenge Questions Can be viewed:"

    def test_4e_Add_Challenge_Question(self):

        time.sleep(1)
        self.tickAddChallQuestions = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[2]/div/div[1]/div[1]/div/i')
        self.tickAddChallQuestions.click()

        time.sleep(1)
        self.addcqmodal = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[1]/h4')
        assert self.addcqmodal.text == 'Add Question'
        if self.addapimodal.text == u'Add Question':
            print "Add Question Modal is Present:"

        self.tickAddChallengeQuestionsTextbox = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[2]/tabset/div/tab/div[1]/div/div/input')
        self.tickAddChallengeQuestionsTextbox.click()

        time.sleep(1)
        ChallengeQuestion = 'Decode it '.join(random.choice(string.ascii_uppercase) for _ in range (2)).join('?')
        self.tickAddChallengeQuestionsTextbox.send_keys(ChallengeQuestion)

        time.sleep(1)
        self.tickaddcq = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[2]/tabset/div/tab/div[2]/div/div/button[1]').click()

        time.sleep(1)
        self.savecq =  self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[2]/div/div[2]/div/div/button')

if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
