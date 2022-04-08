from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(3)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    #confirm = browser.switch_to.alert
    #confirm.accept()


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    #browser.find_element(By.ID, "robotCheckbox").click()
    #browser.find_element(By.ID, "robotsRule").click()




    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


