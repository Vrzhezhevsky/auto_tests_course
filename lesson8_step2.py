from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    summ = int(x) + int(y)

    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("option:nth-child(2)").click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))  # ищем элемент с текстом "Python"


    #browser.find_element(By.TAG_NAME, "select").click()
    #browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    #browser.find_element(By.ID, "robotsRule").click()

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    #button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()