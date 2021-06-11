#from selenium import webdriver

#path = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(path)
#driver.get('http://www.w3schools.com/')
#target = driver.find_element_by_link_text('BROWSE TEMPLATES')
#driver.execute_script('arguments[0].scrollIntoView(true);', target)
file = open("text.txt")
line = file.read()
word = line.split("\n")
print(word)
file.close()

