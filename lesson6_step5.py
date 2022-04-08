from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


if __name__ == '__main__':
    link = "http://suninjuly.github.io/find_link_text"
    #link_part = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        actual_link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
        actual_link.click()
        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()


    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла