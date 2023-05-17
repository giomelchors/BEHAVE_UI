from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TranslatorPage(object):
    def __init__(self, context):
        self.browser = context.browser
        self.config = context.config
        self.timeout = 30

    def open(self, path):
        self.browser.get(path)

    def close(self):
        self.browser.quit()

    def update(self):
        self.browser.refresh()

    def set_atribute(self, action):
        setattr(self.browser, action[0], action[1])

    def click(self, selector):
        try:
            element = TranslatorPage.find(self, selector)
            return element.click()
        except Exception as e:
            print('This Exception has occurred, ' + str(e))
            return e


def find(self, selector, element):
    self.selector = selector
    self.element = element
    try:
        if selector == 'id':
            return self.browser.find_element(By.ID, self.element)
        if selector == 'xpath':
            return self.browser.find_element(By.XPATH, self.element)
    except NoSuchElementException as e:\
        print('This Exception has occurred, ' + str(e))
    return e