import time

from behave import given, when, then, step

from selenium.webdriver.common.keys import Keys
from Features.pages.translator_page import TranslatorPage
from Features.support.data_elements import DataElements


@given("that user want to use the page {page}")
def step_impl(context, page):
    context.web_site = page
    TranslatorPage(context).open(DataElements[context.web_site]['url'])


@when("he select the source language as {Source}")
def step_impl(context, Source):
    target_tab = DataElements[context.web_site]['Target_language_tab']['selector']
    element_tab = DataElements[context.web_site]['Target_language_tab'][target_tab]
    TranslatorPage(context).click(target_tab, element_tab)
    time.sleep(1)
    text_box = DataElements[context.web_site]['Source_Write_Bar']['selector']
    text_box_element = DataElements[context.web_site]['Source_Write_Bar'][text_box]
    text = TranslatorPage(context).find(text_box, text_box_element)
    text.send_keys(Source)
    language_sel = DataElements[context.web_site]['Language_source_selected_bar']['selector']
    element_language_sel = DataElements[context.web_site]['Language_source_selected_bar'][language_sel]
    TranslatorPage(context).click(language_sel, element_language_sel)


@step("select the target language as {Target}")
def step_impl(context, Target):
    source_tab = DataElements[context.web_site]['Source_language_tab']['selector']
    source_element = DataElements[context.web_site]['Source_language_tab'][source_tab]
    TranslatorPage(context).click(source_tab, source_element)
    time.sleep(1)
    text_box = DataElements[context.web_site]['Target_Write_Bar']['selector']
    text_box_element = DataElements[context.web_site]['Target_Write_Bar'][text_box]
    text_source = TranslatorPage(context).find(text_box, text_box_element)
    text_source.send_keys(Target)
    language_sel = DataElements[context.web_site]['Language_target_selected_bar']['selector']
    element_language_sel = DataElements[context.web_site]['Language_target_selected_bar'][language_sel]
    TranslatorPage(context).click(language_sel, element_language_sel)


@step(u'write the sentence {Sentence}')
def step_impl(context, Sentence):
    text_box = DataElements[context.web_site]['text_box']['selector']
    text_box_element = DataElements[context.web_site]['text_box'][text_box]
    text_source = TranslatorPage(context).find(text_box, text_box_element)
    text_source.send_keys(Sentence)
    time.sleep(2)


@then("the screen should display the {sentence}")
def step_impl(context, sentence):
    text_box = DataElements[context.web_site]['text_result']['selector']
    text_box_element = DataElements[context.web_site]['text_result'][text_box]
    actual_text = TranslatorPage(context).find_text(text_box, text_box_element)
    assert actual_text == sentence, "the sentences are different"


