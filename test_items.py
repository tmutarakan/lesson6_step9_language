link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_cart(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, 'The button is missing'
    # from time import sleep
    # sleep(30)
