from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
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

    def find(self, selector, element):
        self.selector = selector
        self.element = element
        try:
            if selector == 'id':
                return self.browser.find_element(By.ID, self.element)
            if selector == 'xpath':
                return self.browser.find_element(By.XPATH, self.element)
        except NoSuchElementException as e: \
                print('This Exception has occurred, ' + str(e))
        return e

    def click(self, selector, element):
        try:
            element = TranslatorPage.find(self, selector, element)
            return element.click()
        except Exception as e:
            print('This Exception has occurred, ' + str(e))
            return e

    def action_enter(self):
        ActionChains(self.browser).send_keys(Keys.ENTER)

    def drop_down(self):
        ActionChains(self.browser).send_keys(Keys.ARROW_DOWN)

    def find_text(self, selector, element):
        try:
            element = TranslatorPage.find(self, selector, element)
            return element.text
        except Exception as e:
            print('This Exception has occurred ' + str(e))
            return e
