from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")


# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#     print(tag.get_text())

heading = soup.find(name="h1", id="name")
# print(heading.string)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

name = soup.select_one(selector="#name")

company_url = soup.select_one(selector="p a")
company_url = company_url.get("href")

headings = soup.select(".heading")
print(company_url)















