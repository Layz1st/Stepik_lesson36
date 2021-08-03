import time
import selenium.common.exceptions


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search__button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    browser.implicitly_wait(5)
    button = False

    try:
        button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    except selenium.common.exceptions.NoSuchElementException:
        assert button, "button not exist"







