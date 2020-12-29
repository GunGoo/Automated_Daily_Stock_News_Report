from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://finviz.com")
elem_search = driver.find_element_by_xpath(
    "/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/form/input")

elem_search.send_keys("XPEV")
elem_search.send_keys(Keys.RETURN)


# driver.get("https://finviz.com/login.ashx")
# elem_id = driver.find_element_by_name("email")
# elem_id.send_keys("")
# elem_pwd = driver.find_element_by_name("password")
# elem_pwd.send_keys("")
# elem_login_btn = driver.find_elements_by_xpath(
#     "/html/body/div[2]/div/div/form/input")[0]
# elem_login_btn.click()

# elem_search = driver.find_element_by_xpath(
#     "/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/div/form/input")

# elem_search.send_keys("XPEV")
# elem_search.send_keys(Keys.RETURN)


# elem = driver.find_element_by_id("search")
# elem.send_keys("XPEV")
# elem.send_keys(Keys.RETURN)
# assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
