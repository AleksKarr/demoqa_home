# from pages.swag_labs import SwagLabs
#
#
# def test_check_swag(browser):
#     swag_page = SwagLabs(browser)
#     swag_page.visit()
#     assert swag_page.exist_icon()

# from pages.swag_labs import SwagLabs
#
#
# def test_check_username_field(browser):
#     swag_page = SwagLabs(browser)
#     swag_page.visit()
#     assert swag_page.find_element(locator="#user-name")


from pages.swag_labs import SwagLabs


def test_check_password_field(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.find_element(locator="#password")