import requests as requests
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml

#
chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSckMgWiqE9qVgq-uS_v2BYPbPZ6ALgtIE9iuPMYaSg812ylQA/viewform?usp=sf_link"

params = {
    "Accept-Language": "en-US,en;q=0.9,mn-MN;q=0.8,mn;q=0.7,ko-KR;q=0.6,ko;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

URL = "https://www.zillow.com/homes/for_rent/2-_beds/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-77.13538077075194%2C%22east%22%3A-76.89333822924803%2C%22south%22%3A38.800225260313695%2C%22north%22%3A38.997947128827064%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22pagination%22%3A%7B%7D%7D"

response = requests.get(url=URL, headers=params)
soup = BeautifulSoup(response.text, parser=lxml, features="lxml")

# Actual addresses of the houses
addresses = soup.select(".list-card-addr")
address = [address.getText() for address in addresses]

# Links to the houses
links = soup.select(".list-card-img")
link = [link.get("href") for link in links if link.get("href")]

# Actual price of the house
prices = soup.select(".list-card-price")
price = [price.getText().split("/")[0] for price in prices]

driver.get(FORMS)
for i in range(len(link)):
    driver.get(FORMS)
    questions = driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput.exportInput")
    questions[0].send_keys(address[i])
    questions[1].send_keys(price[i])
    questions[2].send_keys(link[i])
    button = driver.find_element_by_css_selector(".exportButtonContent")
    button.click()
    driver.implicitly_wait(5)


print(len(address))
print(len(link))

print(len(price))
