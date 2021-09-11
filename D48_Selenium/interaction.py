from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector('#articlecount a')
# article_count.click()

technology = driver.find_element_by_link_text("Technology")
# technology.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
