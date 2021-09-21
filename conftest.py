import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language with command --language")

chrome_cfg = Options()
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')

# Инициализация браузера и сборка мусора
@pytest.fixture(scope="function")
def browser(request):
    print("\nStart browser for case..")
    if request.config.getoption("language") == None:
        raise pytest.UsageError("Choose language with command --language")
    chrome_cfg.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption("language")})  #Добавляем заголовок языка 
    browser = webdriver.Chrome(options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')
    yield browser
    print("\nExit browser for case..")
    browser.quit()

    # хуй