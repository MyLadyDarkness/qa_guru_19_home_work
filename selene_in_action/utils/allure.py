import allure
from selene import browser
import requests
from allure_commons.types import AttachmentType
import config


def attach_bstack_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.bstack_userName, config.bstack_accessKey),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def attach_bstack_screen():
    allure.attach(
        browser.driver.get_screenshot_as_png(), #get_screenshot_as_png(),
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png'
    )

def attach_screen():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )

def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='Screenshot',
                  attachment_type=allure.attachment_type.PNG)


# def add_screenshot(browser):
#     png = browser.driver.get_screenshot_as_png()
#     allure.attach(body=png,
#                   name='screenshot',
#                   attachment_type=allure.attachment_type.PNG,
#                   extension='.png')


def attach_bstack_source(browser):
    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )
