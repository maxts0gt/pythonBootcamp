from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.appbrewery.co/p/newsletter")
# placeholder = driver.find_element_by_css_selector(".form-control")
# placeholder.send_keys("gibberish@gmail.com")
# placeholder.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_css_selector(".top")
first_name.send_keys("Max")
last_name = driver.find_element_by_css_selector(".middle")
last_name.send_keys("Ts")
sign_up = driver.find_element_by_css_selector(".bottom")
sign_up.send_keys("gibberish@gmail.com")
sign_up.send_keys(Keys.ENTER)