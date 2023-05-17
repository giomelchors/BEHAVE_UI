from selenium import webdriver


def before_all(context):
    print("Before scenario\n")
    context.browser = webdriver.Chrome()
