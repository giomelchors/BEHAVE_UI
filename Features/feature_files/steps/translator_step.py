import time

from behave import given, when, then

from selenium.webdriver.common.keys import Keys
from Features.pages.translator_page import TranslatorPage
from Features.support.data_elements import DataElements


@given("that user want to use the page {page}")
def step_impl(context, page):
    context.web_site = page
    TranslatorPage(context).open(DataElements[context.web_site]['url'])




@when("he translate the word {table} from {Target} to {Source}")
def step_impl(context, table, Target, Source):
    target_tab = DataElements[context.web_site]['Target_language_tab']['selector']
    element = DataElements[context.web_site]['Target_language_tab'][target_tab]
    TranslatorPage(context).click(target_tab, element)
    time.sleep(5)
    text_box = DataElements[context.web_site]['Target_Write_Bar']['selector']
    text_box_element = DataElements[context.web_site]['Target_Write_Bar'][text_box]
    text = TranslatorPage(context).find(text_box,text_box_element)
    text.send_keys(Target)
    time.sleep(5)






#@then(u'he should see the word Mesa on the screen')
#def step_impl(context):
