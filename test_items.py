
import time

from selenium import webdriver

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    btn = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert btn > 0, "Кнопка добавления отсутствует"
