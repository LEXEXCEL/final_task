import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language for this site")


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    options = Options()

    if language not in ('ru', 'en', 'ar', 'ca', 'cs', 'da', 'de',
                        'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl',
                        'pl', 'pt', 'pt-br', 'ro', 'sk', 'ur', 'zh-cn'):
        raise pytest.UsageError(f"Unsupported language '{language}'. Please use correct language.")

    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(options=options)

    yield driver

    print("\nquit browser..")
    driver.quit()
