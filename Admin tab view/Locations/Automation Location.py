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


#clicking the PAM & Location
driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[6]/div/tree-node-wrapper/div/div/tree-node-content/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="custom-tree"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[6]/div/tree-node-children/div/tree-node-collection/div/tree-node[6]/div/tree-node-wrapper/div/div/tree-node-content/span').click()
time.sleep(2)

# clicking the Add Location
driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-locations-detail-component/app-master-view/div[1]/div[2]/config-button-component/div/button').click()
time.sleep(2)

# clicking the Manual Button
driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/admin-locations-detail-component/div[2]/div/div/div[2]/div/div[1]/button').click()
time.sleep(1)


# clicking the Location Name
locationname = 'Location  ' + ' - ' +''.join(random.choice(string.ascii_uppercase) for _ in range(5))
driver.find_element_by_id('inputLocationName').send_keys(locationname)
time.sleep(1)

# clicking the Address 1
driver.find_element_by_id('inputAddressOne').send_keys('112 VA Rufino Makati')
time.sleep(1)
driver.find_element_by_id('inputPostalCode').send_keys('3006')
time.sleep(1)
driver.find_element_by_id('inputCity').send_keys('Makati')
time.sleep(1)

# clicking the Country
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-location-modal-component/div/div/div/div[2]/tabset/div/tab/div[1]/country-dropdown/form/div/ng-select/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-location-modal-component/div/div/div/div[2]/tabset/div/tab/div[1]/country-dropdown/form/div/ng-select/select-dropdown/div/div[2]/ul/li[1]').click()
time.sleep(1)


# clicking the Province
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-location-modal-component/div/div/div/div[2]/tabset/div/tab/div[4]/form/div/div/ng-select/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-location-modal-component/div/div/div/div[2]/tabset/div/tab/div[4]/form/div/div/ng-select/select-dropdown/div/div[2]/ul/li[1]').click()
time.sleep(1)




#clicking the Save button
driver.find_element_by_xpath('/html/body/oid-app/my-app/update-location-modal-component/div/div/div/div[2]/tabset/div/tab/div[5]/div/div/button[1]').click()
time.sleep(1)
