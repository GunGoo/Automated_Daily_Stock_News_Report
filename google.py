from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.sec.gov/edgar/searchedgar/companysearch.html")
timeout = 5
search_box = "/html/body/div[2]/div/div/div/section/div[3]/div[2]/div[2]/div[3]/div/form/input[1]"
try:
    element_present = EC.presence_of_element_located(
        (By.XPATH, search_box))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")


elem_search = driver.find_element_by_xpath(search_box)
elem_search.send_keys("APPLE")
time.sleep(3)
elem_search.send_keys(Keys.RETURN)

finan_stat = "/html/body/div[5]/table/tbody/tr[2]/td[1]/div/ul/li[4]/a"

try:
    element_present = EC.presence_of_element_located(By.XPATH, finan_stat)
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

financial_statement = driver.find_element_by_xpath(finan_stat)


# elem_search.send_keys("XPEV")
# elem_search.send_keys(Keys.RETURN)


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
