from selenium import webdriver


def SeleniumBrowser():
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    return webdriver.Edge(options=options)