from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
value = driver.find_elements_by_css_selector(".event-widget div ul li")

items = [item.text for item in value]
events = {i: {"time": item.split("\n")[0], "name": item.split("\n")[1]} for i, item in enumerate(items)}

print(events)

driver.quit()
