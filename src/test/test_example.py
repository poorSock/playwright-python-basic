import re

from playwright.sync_api import Page, expect

def test1(page: Page):
    page.goto('https://www.qualityminds.de')
    expect(page).to_have_title(re.compile("QualityMinds | Startseite"))

def test2(page: Page):
    page.goto('https://www.qualityminds.de')
    expect(page.get_by_role("link", name="KONTAKT", exact=True)).to_have_attribute('href', 'https://qualityminds.com/de/kontakt/')

def test3_SendContactForm(page: Page):
    page.goto('https://www.qualityminds.de')
    page.get_by_role("link", name="KONTAKT", exact=True).click()

    page.locator('[name=et_pb_contact_name_0]').type('Testname')
    page.locator('[name=et_pb_contact_surname_0]').type('Test-Surname')
    page.locator('[name=et_pb_contact_email_0]').type('Test@email.de')
    page.locator('[name=et_pb_contact_message_0]').type('Test Message')

    page.get_by_role("button", name="Senden").click()
    expect(page.locator('[class=et-pb-contact-message]')).to_be_visible()
    expect(page.locator("li").filter(has_text="Ich habe die Datenschutzerklä")).to_be_visible()