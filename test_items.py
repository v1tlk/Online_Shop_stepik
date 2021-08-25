class Test_BookShop:
    
    def test_cart_button(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        assert browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button'), '"Add to cart" button not found'