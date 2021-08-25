import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Test_BookShop:
    def test_cart_button(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        assert browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button'), '"Add to cart" button not found'