from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#test

# 1a.
driver = webdriver.Chrome(executable_path="C:\eliran\DevOps\chromedriver.exe")
# driver.get("http://www.walla.co.il")
# sleep(10)
# # 1b.
# driver = webdriver.Chrome(executable_path="C:\eliran\DevOps\geckodriver.exe")
driver.get("http://www.ynet.co.il")
#
# # 2
# title = driver.title
# driver.refresh()
# if title == driver.title:
#     print("equal")

# 3 yes - elements are the same regardless to the browser

# 4
# driver.get("https://translate.google.co.il/")
# driver.find_element_by_class_name("er8xn").send_keys("אבא")

# # 5
driver.get("http://youtube.com")
driver.find_element_by_name("search_query").send_keys("madona")
sleep(10)
driver.find_element_by_id("search-icon-legacy").click()


# 6
driver.get("https://translate.google.com/")
a = driver.find_element_by_class_name("er8xn").send_keys("אבא")
# b = driver.find_element_by_class_name("jfk-button")
# c = driver.find_element_by_xpath("//input[@type=‘submit']")
# print(a)
#
# # 7
# driver.get("https://www.facebook.com/")
# driver.find_element_by_id("email").send_keys("a@a.com")
# driver.find_element_by_id("pass").send_keys("Aa123456")