import requests

from bs4 import BeautifulSoup


with open("sample.html", "r") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser') # Soup is a special object made by beautiful soup which makes it convenient for it to evaluate data

# print(soup.prettify())
# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div")[0])
# print(type(soup.find_all("div")[0]))

# for link in soup.find_all("a"):
#     print(link.get("href"))

# link1 = soup.find(id="link1")
# print(link1.get("href"))

# print(soup.select("div.italic")[0].get_text())
# print(soup.select("span#italic"))
# print(soup.span.get("class"))

# print(soup.find(class_="italic"));

# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)

# modifying elements
# container = soup.find(class_="container")
# container.name = "span"
# container["class"] = "newClass class2"
# container.string = "I am a string"
# print(container);

# # Inserting new tags
# ulTag = soup.new_tag("ul")
# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)

# # Saving in file the new HTML
# with open("modified.html", "w") as f:
#     f.write(str(soup))

container = soup.find(class_="container")
print(container.has_attr("id"))

def hasIdNotClass(tag):
    return tag.has_attr("id") and not tag.has_attr("class")

results = soup.find_all(hasIdNotClass)

print(results)