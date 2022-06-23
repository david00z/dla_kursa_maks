from selenium import webdriver 
import time 
import math


 
link = "http://suninjuly.github.io/math.html" 
 
try: 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome() 
    browser.get(link) 
    x_element = browser.find_element_by_id("input_value") 
    
    x = x_element.text
    y = calc(x)
    x_element.send_keys('y')
    input1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    input1.click()
    input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    input2.click()
    button = browser.find_element_by_class_name("btn btn-default") 
    button.click() 
 
finally: 
    # успеваем скопировать код за 30 секунд 
    time.sleep(30) 
    # закрываем браузер после всех манипуляций 
    browser.quit() 
 
# не забываем оставить пустую строку в конце файла
