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


    def test_1a_Log_in_with_Invalid_Credentials(self):
        #Invalid username
        self.driver.implicitly_wait(2)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.send_keys("narman@test.com")
        self.driver.implicitly_wait(2)
        self.loginbtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/input')
        self.loginbtn.click()
        self.driver.implicitly_wait(2)
        #Invalid Password
        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.send_keys("Invalid")
        #Login
        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        self.driver.implicitly_wait(2)
        self.invalidmessage = self.driver.find_element_by_tag_name('p')
        assert self.invalidmessage.text == 'Your login attempt was not successful.'
        if self.invalidmessage.text == u'Your login attempt was not successful.':
            print ("Verify invalid login:")

    def test_1b_Log_in_with_Valid_Credentials(self):
        self.driver.implicitly_wait(2)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.clear()
        self.user_name.send_keys("release@test.com")
        self.driver.implicitly_wait(2)

        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.clear()
        self.password.send_keys("R0cknit!")

        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        self.driver.implicitly_wait(2)
        self.testlogin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/connections-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.testlogin.text == 'Search All Connections'
        if self.testlogin.text == u'Search All Connections':
            print ("Verify valid login:")

    def test_2a_Admin(self):
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
            print "Admin Tab Present:"


    def test_2b_Account_Administration(self):
        #Go to Account Administration
        self.driver.implicitly_wait(2)
        self.accntadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/tree-node-expander/span')
        self.driver.implicitly_wait(2)
        self.accntadmin.click()
        self.driver.implicitly_wait(2)
        #Go to API Keys
        self.api = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.api.click()
        self.driver.implicitly_wait(2)
        #Add api key button
        self.addapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/tapik-component/app-master-view/div[1]/div[2]/config-button-component/div/button')
        self.addapi.click()
        time.sleep(1)
        self.driver.implicitly_wait(2)

        #Assert if Add API Modal is present
        time.sleep(2)
        self.addapimodal = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[1]/h4')
        assert self.addapimodal.text == 'Add API Key'
        if self.addapimodal.text == u'Add API Key':
            print "Add API Modal is Present:"

    def test_2c_View_API_Keys(self):

        time.sleep(2)
        self.driver.implicitly_wait(2)
        self.viewapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/tapik-component/app-master-view/div[1]/div[1]/h3')
        assert self.viewapi.text == 'API Keys'
        if self.viewapi.text == u'API Keys':
            print "Verify API Keys Can be viewed:"

    def test_2d_Add_API_KEY_with_default_Expiration(self):
        #add api
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apiname = self.driver.find_element_by_xpath('//*[@id="inputName"]')
        apiname = 'Automated Test '.join(random.choice(string.ascii_lowercase) for _ in range (2))
        self.apiname.send_keys(apiname) #api name

        #Add api key description
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.desapi = self.driver.find_element_by_xpath('//*[@id="inputDescription"]')
        des = 'Description'
        self.desapi.send_keys(des) #api description

        #Add api key email
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apiemail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        apiemail = 'arman.navarro@teravibe.com'
        self.apiemail.send_keys(apiemail) #api email

        #select Role
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apirole = self.driver.find_element_by_xpath('//*[@id="inputUserRoles"]/div/div/input')
        self.apirole.click()
        self.driver.implicitly_wait(2)
        self.pickrole = self.driver.find_element_by_xpath('//*[@id="inputUserRoles"]/select-dropdown/div/div/ul/li[1]')
        self.pickrole.click()
        self.driver.implicitly_wait(2)

        #select user groups
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apigroup = self.driver.find_element_by_xpath('//*[@id="inputUserGroups"]/div/div/input')
        self.apigroup.click()
        self.driver.implicitly_wait(2)
        self.picgroup = self.driver.find_element_by_xpath('//*[@id="inputUserGroups"]/select-dropdown/div/div/ul/li[1]')
        self.picgroup.click()

        #save_api
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.saveapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[4]/div/confirm-cancel-component/div/button[1]')
        self.saveapi.click()

    def test_3d_Challenge_Questions(self):
        #Assert if challenge question is present
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.vercq = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.vercq.text == 'Challenge Questions'
        if self.vercq.text == u'Challenge Questions':
            print "Verify Challenge Questions is Present from the tree:"

    def test_4d_View_Challenge_Questions(self):
        #navigate to challenge questions
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
            print "Verify Challenge Questions Can be viewed:"

    def test_4e_Add_Challenge_Question(self):

        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.tickAddChallQuestions = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div/div[2]/div/div[1]/div[1]/div/i')
        self.tickAddChallQuestions.click()

        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.addcqmodal = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-challenge-questions-detail-component/div[2]/div/div/div[1]/h4')
        assert self.addcqmodal.text == 'Add Question'
        if self.addcqmodal.text == u'Add Question':
            print "Add Question Modal is Present:"

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

    def test_5a_View_Configuration_Parameters(self):

        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.confpick = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[3]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.confpick.click()

        self.driver.implicitly_wait(2)
        time.sleep(2)
        self.viewconfparams = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[1]/div/h4')
        assert self.viewconfparams.text == 'Configuration Parameters'
        if self.viewconfparams.text == u'Configuration Parameters':
            print "Verify Configuration Parameters Can be viewed:"
        self.driver.implicitly_wait(2)
        time.sleep(1)

    def test_5b_Update_Configuration_Parameters(self):
        #Navigate to configuration parameter section
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.confpick = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[3]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.confpick.click()
        #Select a default agent type dropdown
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.tickdefagent = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[2]/td/div/form/div/div/ng-select/div/div/div[1]')
        self.tickdefagent.click()
        #Pick user as default agent type
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.pickuser = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[2]/td/div/form/div/div/ng-select/select-dropdown/div/div[2]/ul/li[1]')
        self.pickuser.click()
        #Select a default gateway agent dropdown
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.defgate = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[3]/td/div/form/div/div/agent-dropdown/form/div/ng-select/div/div/div[1]')
        self.defgate.click()
        #Select or pick  gateway agent from the dropdown
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.selgate = self.driver.find_element_by_xpath('//*[@id="agentSelect"]/select-dropdown/div/div[2]/ul/li[9]')
        self.selgate.click()
        #Turn on session replay
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.onsession = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[4]/td/div/div[2]/div/fieldset/div[1]/label/input')
        self.onsession.click()
        #SElect or input a mfa knock response time-out
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.mfaknockres = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[6]/td/div/div[2]/div/div/input')
        self.mfaknockres.clear()
        self.mfaknockres.click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        knockres = "120"
        self.mfaknockres.send_keys(knockres)
        #Select or input a user secondary verification expiry in minutes
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.usersecondaryexpiry = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[8]/td/div/div[2]/div/div/input')
        self.usersecondaryexpiry.clear()
        self.usersecondaryexpiry.click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        usersecondaryexpiry = "10"
        self.usersecondaryexpiry.send_keys(usersecondaryexpiry)
        #Select or choose a user secondary verification max resends
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.usersecondarymaxsend = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[10]/td/div/div[2]/div/div/input')
        self.usersecondarymaxsend.clear()
        self.usersecondarymaxsend.click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        usersecondarymaxsend = "10"
        self.usersecondarymaxsend.send_keys(usersecondarymaxsend)
        #select or choose a session time out in minutes
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.sessiontimeout = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[11]/td/div/div[2]/div/div/input')
        self.sessiontimeout.clear()
        self.sessiontimeout.click()

        self.driver.implicitly_wait(2)
        time.sleep(1)
        sessiontimeout = "60"
        self.sessiontimeout.send_keys(sessiontimeout)

        #Pick user secondary verification for oob
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.onsecoob = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[14]/td/div/div[2]/div/fieldset/div[1]/label/input')
        self.onsecoob.click()

        #Pick mfa self enrollment on
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.mfaselfon = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[15]/td/div/div[2]/div/fieldset/div[1]/label/input')
        self.mfaselfon.click()

        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.onusersecafter = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[16]/td/div/div[2]/div/fieldset/div[1]/label/input')
        self.onusersecafter.click()
        #Open the secondary verification types dropdown
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.selectuservertypes = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[17]/td/div/form/div/div/ng-select/div/div')
        self.selectuservertypes.click()
        #pick knock
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.knockselect = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[17]/td/div/form/div/div/ng-select/select-dropdown/div/div/ul/li[4]')
        self.knockselect.click()
        """#pick OTP
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.otpselect = self.driver.find_element_by_xpath('//*[@id="publishTypes"]/select-dropdown/div/div/ul/li[3]')
        self.otpselect.click()
        #pick text
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.textselect = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[17]/td/div/form/div/div/ng-select/select-dropdown/div/div/ul/li[1]')
        self.textselect.click()
        #pick Email
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.emailselect = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[17]/td/div/form/div/div/ng-select/select-dropdown/div/div/ul/li[2]')
        self.emailselect.click()"""

        #Key loggin as on
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.keyon = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[1]/table/tbody/tr[18]/td/div/div[2]/div/fieldset/div[1]/label')
        self.keyon.click()

        #update all Changes
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.updateconfparams = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-configparams-detail-component/div/div[2]/div/div[2]/div/div/button')
        self.updateconfparams.click()

    def test_6a_View_Password_Policy(self):

        self.driver.implicitly_wait(2)
        time.sleep(2)
        self.navpasspol = self.driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[4]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.navpasspol.click()

        self.driver.implicitly_wait(2)
        time.sleep(2)
        self.passpol = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[1]/div/h4')
        assert self.passpol.text == 'Password Policy'
        if self.passpol.text == u'Password Policy':
            print "Verify Password Policy Can be viewed:"

    def test_6b_Update_Password_Policy(self):
        #change Password length
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.passlength = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[1]/div/div[1]/div/div/input')
        self.passlength.clear()
        self.passlength.click()
        passlength = "7"
        self.passlength.send_keys(passlength)

        #Update password expiry Length
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.passexplenght = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[1]/div/div[2]/div/div/input')
        self.passexplenght.clear()
        self.passexplenght.click()
        passexplenght = "30"
        self.passexplenght.send_keys(passexplenght)

        #Password must include number Checkbox
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.passnumber = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[1]/div/div[3]/div/div/div/label')
        self.passnumber.click()

        #Password must include Uppercase
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.passupper = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[1]/div/div[4]/div/div/div/label')
        self.passupper.click()

        #Pass must include a special click_include_special_characters
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.passspecial = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[1]/div/div[5]/div/div/div/label')
        self.passspecial.click()

        #Update failed attempts before locked
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.failedattempts = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[1]/div/div[6]/div/div/input')
        self.failedattempts.clear()
        self.failedattempts.click()
        failedattempts = "20"
        self.failedattempts.send_keys(failedattempts)

        #Save Changes
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.passsave = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-credential-policy-detail-component/div/div[2]/div/div[2]/div/div/button')
        self.passsave.click()

    def test_7a_View_Agent_Maintenance(self):

        #Navigate to agent maintenance main view
        self.driver.implicitly_wait(2)
        time.sleep(2)
        self.agentmain = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.agentmain.click()

        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.agentmainview = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-agents-detail-component/header-component/div/div[1]/h3')
        assert self.agentmainview.text == 'Agent Maintenance'
        if self.agentmainview.text == u'Agent Maintenance':
            print "Verify Agent Maintenance Can be viewed:"

if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
