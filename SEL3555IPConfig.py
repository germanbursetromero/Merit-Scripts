from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

username=""    # change to merit username
password=""    # change based off project
name=""        # change based off device
location = "SCADA Rack"
description = "Backup PPC"
ipaddrOne1=""    # change based off device
ipaddrOne5 =     # change based off device
gateway1 = ""    # change based off device
ipaddrTwo1 = ""  # change based off device
ipaddrTwo5 = ""  # change based off device

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://")

##### This should be commented out if you don't 
##### have to log in for the first time
usname=driver.find_element("id","username")
usname.send_keys(username)

adword=driver.find_element("id","admin_password")
adword.send_keys(password)

adcword=driver.find_element("id","confirm_password")
adcword.send_keys(password)

driver.find_element("name","btnSubmit").click()

time.sleep(5)
##### This should be commented out if you don't 
##### have to log in for the first time

uname=driver.find_element("id","username")
uname.send_keys(username)

pword=driver.find_element("id","txtPassword")
pword.send_keys(password)

driver.find_element("name","submit").click()
time.sleep(5)

driver.find_element("id", "device_name").clear()
driver.find_element("id", "device_name").send_keys(name)
driver.find_element("id", "location").clear()
driver.find_element("id", "location").send_keys(location)
driver.find_element("id", "dev_description").clear()
driver.find_element("id", "dev_description").send_keys(description)
driver.find_element("id", "device_info_save").click()
time.sleep(10)

driver.find_element("id","Interface").click()
time.sleep(5)

driver.find_element("id","edit_0").click()
time.sleep(10)

# if running more than once, this will uncheck ping
driver.find_element("id","ping").click()

driver.find_element("id","ipv4_address1").clear()
driver.find_element("id","ipv4_address1").send_keys(ipaddrOne1)

driver.find_element("id","ipv4_address5").clear()
driver.find_element("id","ipv4_address5").send_keys(ipaddrOne5)

driver.find_element("id", "gateway").clear()
driver.find_element("id","gateway").send_keys(gateway1)
driver.find_element("id", "primary_gw").click()

driver.find_element("id","submitter").click()
time.sleep(10)

driver.find_element("id", "edit_1").click()
time.sleep(10)

driver.find_element("id","ping").click()

driver.find_element("id","ipv4_address1").clear()
driver.find_element("id","ipv4_address1").send_keys(ipaddrTwo1)

driver.find_element("id","ipv4_address5").clear()
driver.find_element("id","ipv4_address5").send_keys(ipaddrTwo5)

driver.find_element("id","submitter").click()

time.sleep(10)
driver.find_element("id","logout").click()


