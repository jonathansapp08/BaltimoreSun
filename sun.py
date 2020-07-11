from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
driver.get("https://www.baltimoresun.com/search/mckenna%20oxenden/100-y/ALL/date/1/")

story_list = []
stories = driver.find_elements_by_class_name('no-u')

for element in stories:
    story_list.append(element.text)

number = 0
print('Select the story you want to read:')
for story in story_list:
    print(str(number) + ' ' + (story_list[number]))
    number = number + 1

selection = int(input("\n"))

driver.find_element_by_link_text(story_list[selection]).click()

article=driver.find_element_by_xpath("//*[@id='f1cQNM16oBRv3s']/div[2]")

print(article.text)