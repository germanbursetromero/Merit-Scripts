from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

username=""      # username used in all machines
password=""      # change based off project name
httpsaddress="downloads.dell.com"
snmpname="private"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://")


##LOGIN##
time.sleep(5)
uname=driver.find_element("name", "username")
uname.send_keys(username)

pword=driver.find_element("name", "password")
pword.send_keys(password)

driver.find_element(By.CLASS_NAME, "cux-button").click()
time.sleep(10)
##LOGIN##

##SNMP NAME & TLS CHANGE##
driver.find_element("id", "settings").click()
time.sleep(10)

#driver.find_element(By.XPATH, "//a[text()='Services']").click()
element0 = driver.find_element(By.XPATH, "//a[text()='Services']")
driver.execute_script("arguments[0].click();", element0)
time.sleep(5)

driver.find_element(By.XPATH, "//label[text()='SNMP Agent']").click()
time.sleep(2)

# ERRORS AFTER THIS LINE #######################################

#driver.find_element(By.XPATH, "//input[@id='settings.services.snmp.AgentCommunity']").clear()

#driver.find_element(By.XPATH, "//input[@id='settings.services.snmp.AgentCommunity']").send_keys(snmpname)
element2 = driver.find_element("id", "settings.services.snmp.AgentCommunity")
element2.click() 
time.sleep(1)
element2.clear()
time.sleep(1)
element2.send_keys(snmpname)
time.sleep(3)

#driver.find_element(By.CSS_SELECTOR, "button[ng-switch-when='apply']").click()
wait = WebDriverWait(driver, 5)     # have yet to try this and EC.element_to_be_clickable (if not use driver.find_element)
element3 = wait.until(EC.element_to_be_clickable(By.XPATH, "//button[text()='Apply']"))
element3.click()
time.sleep(5)

#driver.find_element(By.XPATH, "//button[text()='Ok']").click()
element4 = driver.find_element(By.XPATH, "//button[text()='Ok']")
time.sleep(1)
element4.click()
#driver.execute_script("arguments[0].click();", element4)
time.sleep(2)

# driver.find_element(By.XPATH, "//a[text()='Services']").click()
# time.sleep(2)

# driver.find_element(By.XPATH, "//label[text()='Web Server']").click()
# time.sleep(2)

# driver.find_element(By.XPATH, "//label[text()='SNMP Agent']").click()
# time.sleep(2)

# dropdown = driver.find_element("id", "services.webserver.settings.TLSProtocol")
# time.sleep(2)

# select = Select(dropdown)
# select.select_by_value("string:TLS 1.3 Only")
# time.sleep(2)

# driver.find_element(By.XPATH, "//button[text()='Apply']").click()
# time.sleep(3)

# driver.find_element(By.XPATH, "//button[text()='Ok']")
# time.sleep(3)

# driver.find_element(By.XPATH, "//button[text()='Ok']")
# time.sleep(5)
##SNMP NAME & TLS CHANGE##

##UPDATES##
# time.sleep(10)
# driver.find_element("id", "maintenance").click()
# time.sleep(8)

# driver.find_element(By.LINK_TEXT, "System Update").click()
# time.sleep(5)

# dropdown = driver.find_element("id", "FWUpdate.location")
# time.sleep(2)

# select = Select(dropdown)
# select.select_by_value("string:https")
# time.sleep(2)

# driver.find_element("id", "Network.Share.networkShare.nwIPAddress").send_keys(httpsaddress)
# time.sleep(2)

# driver.find_element(By.XPATH, "//button[text()='Check for Update']").click()
# time.sleep(25)

# driver.find_element(By.XPATH, "//input[@ng-click='toggleCheckedAll()']").click()
# time.sleep(3)

# driver.find_element(By.XPATH, "//button[@ng-click='installFW()']").click()
# time.sleep(5)

# driver.find_element(By.XPATH, "//a[text()='Job Queue']").click()
##UPDATES##
