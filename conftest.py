import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_cfg = Options()
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')

# Инициализация браузера и сборка мусора
@pytest.fixture
def browser():
    print("\nStart browser for case..")
    global browser
    browser = webdriver.Chrome(options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')
    yield browser
    print("\nExit browser for case..")
    browser.quit()