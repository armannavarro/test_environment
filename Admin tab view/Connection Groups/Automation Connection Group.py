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


#clicking the PAM & Connection Group
driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[6]/div/tree-node-wrapper/div/div/tree-node-content/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[6]/div/tree-node-children/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span').click()
time.sleep(2)

# clicking the Add Connection Group
driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-connectiongroups-detail-component/app-master-view/div[1]/div[2]/config-button-component/div/button').click()
time.sleep(2)


# clicking the Connection Group Name
connectiongroupname = 'Connection Group ' + ' - ' +''.join(random.choice(string.ascii_uppercase) for _ in range(5))
driver.find_element_by_id('inputConnectionGroupName').send_keys(connectiongroupname)
time.sleep(1)

# clicking the Connection Group Name
connectiongroupdesc = 'Description '
driver.find_element_by_id('inputConnectionGroupDescription').send_keys(connectiongroupdesc)
time.sleep(1)


#choosing location & target
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[4]/div[1]/ng-select/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[4]/div[1]/ng-select/select-dropdown/div/div[2]/ul/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[4]/div[2]/ng-select/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[4]/div[2]/ng-select/select-dropdown/div/div[2]/ul/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[5]/div/ag-grid-angular/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]/span/span[1]/span[2]').click()
time.sleep(1)

#clicking the Add Selected
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[4]/div[3]/button').click()
time.sleep(1)

#clicking the Save button
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-connectiongroups-modal-component/div[1]/div/div/div[2]/tabset/div/tab/div[8]/div/div/button[1]').click()
time.sleep(1)
