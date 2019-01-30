import datetime
import time
import string
import random



from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


wordstack = ["Test", "170", "Multi", "Platform", 'Demo']

driver = webdriver.Chrome("/Users/Cori/Downloads/chromedriver3")
driver.get("https://test.id.overwatchid.com")
# driver.maximize_window()
chrome_options.add_argument("--start-maximized")

#1st login page
time.sleep(2)
username = driver.find_element_by_id("j_username")
username.send_keys("cori@test.com")
time.sleep(2)
driver.find_element_by_class_name('login-button').click()


#2nd login page
password = driver.find_element_by_id("j_pwd")
time.sleep(2)
password.send_keys("password")
time.sleep(2)
driver.find_element_by_class_name('login-button').click()
time.sleep(2)


#clicking the admin tab
driver.find_element_by_xpath('/html/body/oid-app/my-app/div[2]/div[2]/ul/li[4]').click()
time.sleep(2)


#clicking the PAM & Domain
driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[6]/div/tree-node-wrapper/div/div/tree-node-content/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[6]/div/tree-node-children/div/tree-node-collection/div/tree-node[4]/div/tree-node-wrapper/div/div/tree-node-content/span').click()
time.sleep(2)


#clicking the Add Button Domain

driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-domains-detail-component/app-master-view/div[1]/div[2]/config-button-component/div/button').click()
time.sleep(1)

#clicking Domain Name
domainname = 'Domain Name ' + ' - ' +''.join(random.choice(string.ascii_uppercase) for _ in range(5))
driver.find_element_by_id('inputDomainName').send_keys(domainname)
time.sleep(1)

#clicking Domain Manage Target
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-domain-modal-component/div/div/div/div[2]/tabset/div/tab/div[1]/form/div/div/ng-select/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-domain-modal-component/div/div/div/div[2]/tabset/div/tab/div[1]/form/div/div/ng-select/select-dropdown/div/div[2]/ul/li[1]').click()
time.sleep(1)

#clicking Save button
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-domain-modal-component/div/div/div/div[2]/tabset/div/tab/div[2]/div/div/button[1]').click()
time.sleep(1)

# for count in range (1,50):
#
#     time.sleep(2)
#     driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-connectiongroups-detail-component/div[2]/div[1]/div[3]').click()
#     #^plus sign
#     time.sleep(2)
#     connectiongroupname = 'Connection Group Name - Auto ' + ' - ' +''.join(random.choice(string.ascii_uppercase) for _ in range(5))
#     driver.find_element_by_id("inputConnectionGroupName").send_keys(connectiongroupname)
#     time.sleep(.5)
#     connectiongroupdescription = str(count) + ' - ' + ''.join(random.choice(wordstack)) + '-Tenant'
#     time.sleep(.5)
#     driver.find_element_by_id("inputConnectionGroupDescription").send_keys(connectiongroupdescription)
#     time.sleep(1)
#     driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[2]/form/div/div/ng-select/div/div/input').click()
#     time.sleep(1)
#     driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[2]/form/div/div/ng-select/select-dropdown/div/div/ul/li[2]').click()
#     # driver.find_element_by_id("inputEmail").send_keys(apigenerateemail)
#     # time.sleep(.5)
#     # driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[2]/form/div/div/ng-select/div/div/input').click()
#     # time.sleep(.5)
#     # driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[3]/user-groups-dropdown/form/div/div/ng-select/select-dropdown/div/div/ul/li[2]').click()
#     # time.sleep(.5)
#     # driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[2]/form/div/div/ng-select/select-dropdown/div/div/ul/li[2]').click()
#     # time.sleep(.5)
#     # driver.find_element_by_xpath('//*[@id="inputUserRoles"]/select-dropdown/div/div/ul/li[2]').click()
#     # time.sleep(.5)
#     driver.find_element_by_class_name('btn-success').click()
#     time.sleep(.5)
#     count = count + 1
#
# # apiemail = driver.find_element_by_id("inputEmail")
# # time.sleep(1)
# # apiname.send_keys("")
#
#
#
# # username.send_keys("cori.com")
# # password.send_keys("Password1!")
# # driver.implicitly_wait(5)
# # driver.find_element_by_class_name('recaptcha-checkbox-checkmark').click()
#
# # count = 1
# # while count < 6:
# # username and password
