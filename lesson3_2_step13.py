import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_registration_form(self):
        link = "http://suninjuly.github.io/registration1.html"
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.XPATH, "//input[contains(@class, 'first')and @required]").send_keys("Ivan")
        browser.find_element(By.XPATH, "//input[contains(@class, 'second')and @required]").send_keys("Petrov")
        browser.find_element(By.XPATH, "//input[contains(@class, 'third')and @required]").send_keys(
            "ivan@petrov.sm")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)








    def test_registration_form_modified(self):
        link = "http://suninjuly.github.io/registration1.html"
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.XPATH, "//input[contains(@class, 'first')and @required]").send_keys("Ivan")
        browser.find_element(By.XPATH, "//input[contains(@class, 'second')and @required]").send_keys("Petrov")
        browser.find_element(By.XPATH, "//input[contains(@class, 'third')and @required]").send_keys(
            "ivan@petrov.sm")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()