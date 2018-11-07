from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import os


input = {"google-me": ["Nextel","telefonia do futuro","selenium python"]}
count = 3

def searching(keys):
    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = Firefox(options=opts)
    browser.get("https://www.google.com/search?source=hp&ei=1SDiW_LlF8iWwQS2yYeACQ&q=" + keys)
    search = browser.find_elements_by_class_name('iUh30')

    for i in range(count):
        print(search[i].text)


def searchingJson(keys):
    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = Firefox(options=opts)
    browser.get("https://www.google.com/search?source=hp&ei=1SDiW_LlF8iWwQS2yYeACQ&q=" + keys)
    search = browser.find_elements_by_class_name('iUh30')

    result = []

    for i in range(count):
        result.append(search[i].text)

    output = {keys: result}
    saveOut = str(output).replace("'", '"')
    print (saveOut)

    archive = open("output.json","a")
    archive.write(saveOut)
    archive.write("\n")
    archive.close()

print ("------> Retonando os 3 primeiros resultados para cada chave listada <------")
for keys in input["google-me"]:
    searching(keys)

print ("\n---> Retonando o json dos 3 primeiros resultados para cada chave listada <---")

if os.path.exists("output.json"):
    print ("***\nComo o arquivo output.json já existe, \no mesmo sera removido e recriado logo em seguida\n***")
    os.remove("output.json")

for keys in input["google-me"]:
    searchingJson(keys)
