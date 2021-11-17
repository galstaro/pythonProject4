from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import locale
from home_page_class import home_page
from category_page_class import category_page
from product_page_class import product_page
from shopping_cart_page_class import shopping_cart_page
from order_payment_page_class import order_payment_page
from create_account_page_class import create_account_page
from my_orders_page_class import my_orders_page
from unittest import TestCase
from sheet import AOS_Sheet
from selenium.common import exceptions


class tests_AOS(TestCase):
    def setUp(self):
        print("setUp")
        service1 = Service(r"C:\chromedriver_win32/chromedriver")
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get("https://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait=WebDriverWait(self.driver,10)
        self.home=home_page(self.driver)
        self.category=category_page(self.driver)
        self.product=product_page(self.driver)
        self.shopping_cart_page = shopping_cart_page(self.driver)
        self.order_payment=order_payment_page(self.driver)
        self.create_account=create_account_page(self.driver)
        self.my_orders=my_orders_page(self.driver)
        self.sheet = AOS_Sheet()

    def tearDown(self):
        sleep(2)
        self.driver.close()
        print("tearDown")

    # Test 1- choose 3 products by different quantities and check if the cart was updated
    def test1(self):
        total_items=0
        for i in range(3):
            self.home.click_category(1,i+1)
            self.category.click_product(1,i+1)
            quantity=self.product.enter_quantity(1,i+1)
            total_items+=quantity
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        number_of_items = self.home.total_items_in_cart()
        # Check if the total of items that we added to cart equal to the total items in shopping cart window.
        self.assertEqual(total_items, int(number_of_items))
        if total_items==int(number_of_items):
            # add pass_or_fail method insert to the xl sheet the result of the test
            self.sheet.add_pass_or_fail(1,1)

    # Test2 - check if products details which we added to cart have the same details in the shopping cart window.
    def test2(self):
        quantities=[]
        colors=[]
        names=[]
        prices=[]
        for i in range(3):
            self.home.click_category(2, i + 1)
            self.category.click_product(2, i + 1)
            quantity = self.product.enter_quantity(2, i + 1)
            quantities.append(quantity)
            color=self.product.choose_color(2,i+1)
            colors.append(color)
            product_name=self.product.product_name()
            names.append(product_name)
            price=self.product.price()
            prices.append(float(price))
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        names.reverse()
        # Check if the products names equal to the names in the shopping cart window
        self.assertListEqual(names,self.home.names_in_cart())
        quantities.reverse()
        # Check if the products quantities equal to the quantities in the shopping cart window
        self.assertListEqual(quantities,self.home.quantities_in_cart())
        colors.reverse()
        prices.reverse()
        # Check if the products colors equal to the colors in the shopping cart window
        self.assertListEqual(self.home.colors_in_cart(), colors)
        expected_price = 0.0
        for i in range(3):
            expected_price += quantities[i] * prices[i]
        # Check if the products total price equal to the total price in the shopping cart window
        self.sheet.add_pass_or_fail(2, round(expected_price,2) == self.home.price())
        self.assertEqual(round(expected_price,2),self.home.price())

    # Test 3 - check if remove button in shopping cart window actually works
    def test3(self):
        for i in range(3):
            self.home.click_category(3, i + 1)
            self.category.click_product(3, i + 1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()

        number_of_products=self.home.len_of_products_in_Cart()
        self.home.click_remove()
        number_products_after_remove=self.home.len_of_products_in_Cart()
        self.sheet.add_pass_or_fail(3, number_of_products == number_products_after_remove+1)
        # Check if the number of products before remove one is greater than after remove one in one product difference
        self.assertEqual(number_of_products,number_products_after_remove+1)

    # Test 4 - check if you click on cart item shopping cart page is opened
    def test4(self):
        self.home.click_category(4, 1)
        self.category.click_product(4, 1)
        self.product.click_add_to_cart()
        self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        text=self.shopping_cart_page.title_text_shopping_cart()
        self.sheet.add_pass_or_fail(4, text=='SHOPPING CART')
        # Check if the title of the page equals to "SHOPPING CART"
        self.assertEqual(text,'SHOPPING CART')

    # Test 5 - check if the products total price equal to the total price in the shopping cart window
    def test5(self):
        quantities = []
        names = []
        prices = []
        for i in range(3):
            self.home.click_category(5,i + 1)
            self.category.click_product(5,i+1)
            quantity = self.product.enter_quantity(5,i+1)
            quantities.append(quantity)
            product_name = self.product.product_name()
            names.append(product_name)
            price = self.product.price()
            prices.append(float(price))
            print(f"name: {product_name}, quantity: {quantity}, price: {float(price)}")
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        total_price=self.shopping_cart_page.price()
        expected_price=0.0
        for i in range(3):
            expected_price += quantities[i] * prices[i]
        print(expected_price,total_price)
        total_price=float(total_price)
        total_price=round(total_price,2)
        self.sheet.add_pass_or_fail(5, round(expected_price,2) == total_price)
        # Check if the products total price equal to the total price in the shopping cart window
        self.assertEqual(round(expected_price,2),total_price)

    # Test 6- add 3 products to cart and click edit to change there quantities and check if they were updated
    def test6(self):
        # add to cart 3 products
        for i in range(3):
            self.home.click_category(6, i + 1)
            self.category.click_product(6, i + 1)
            self.product.enter_quantity(6,i+1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        edits=self.shopping_cart_page.edit()
        before_change_quantities=self.shopping_cart_page.quantities_in_cart()
        # click edit for each product and change their quantities
        for x in range(len(edits)):
            edits2=self.shopping_cart_page.edit()
            edits2[x].click()
            self.product.change_quantity()
            self.product.click_add_to_cart()
        pass_or_fail=True
        after_change_quantities = self.shopping_cart_page.quantities_in_cart()
        print(before_change_quantities)
        print(after_change_quantities)
        # check if the quantities were updated
        for i in range(len(after_change_quantities)):
            if before_change_quantities[i]==after_change_quantities[i]:
                pass_or_fail=False
                break
        self.sheet.add_pass_or_fail(6,pass_or_fail)
        self.assertTrue(pass_or_fail)

    # Test 7- add tablet product to the cart and the path to the product
    def test7(self):
        # go to product from tablets category
        self.home.click_category(7,1)
        self.category.click_product(7,1)
        self.driver.back()
        # check if the driver took us to Tablets
        self.assertEqual(self.category.category_title(),"TABLETS")
        self.driver.back()
        # check if the driver took us to home page
        self.assertTrue(self.home.check_if_page_is_home())
        self.sheet.add_pass_or_fail(7,self.home.check_if_page_is_home())

    # Test 8 - E2E test of the AOS site
    def test8(self):
        # add to cart 3 products
        for i in range(3):
            self.home.click_category(8, i + 1)
            self.category.click_product(8, i + 1)
            self.product.enter_quantity(8, i + 1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        self.shopping_cart_page.click_checkout()
        # register to site with new account
        self.order_payment.click_registration()
        self.create_account.enter_username()
        self.create_account.enter_email()
        self.create_account.enter_password()
        self.create_account.enter_confirm_password()
        self.create_account.click_conditions_of_use_agreement()
        self.create_account.click_register()
        self.order_payment.click_next()
        # connect to Safe pay account
        self.order_payment.enter_safe_pay_username()
        self.order_payment.enter_safe_pay_password()
        # pay for the products
        self.order_payment.click_pay_now()
        order_number_inorder_payment = self.order_payment.order_number().text
        # check payment is completed
        self.assertTrue(self.order_payment.completed_payment().is_displayed())
        self.home.click_shopping_cart_window()
        # check shopping cart is empty
        self.assertTrue(self.shopping_cart_page.shopping_cart_empty().is_displayed())
        self.home.user_emoji_click()
        self.home.click_my_orders()
        print(order_number_inorder_payment)
        print(self.my_orders.order_numbers())
        # check if the order number is in my orders
        self.sheet.add_pass_or_fail(8,order_number_inorder_payment in self.my_orders.order_numbers())
        self.assertTrue(order_number_inorder_payment in self.my_orders.order_numbers())

    # Test9 - E2E existing user using Master card account
    def test9(self):
        # add to cart 3 products
        for i in range(3):
            self.home.click_category(9,i+1)
            self.category.click_product(9,i+1)
            self.product.enter_quantity(9,i+1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        self.home.click_checkout()
        # login to user
        self.order_payment.enter_username("elad1234")
        self.order_payment.enter_password("Thbyrby145")
        self.order_payment.click_login()
        self.order_payment.click_next()
        # insert Master Card account details
        self.order_payment.click_master_credit()
        self.order_payment.click_edit()
        self.order_payment.fill_master_card_details("123456789123","432", "elad-ratner", "2", "4")
        # pay for order
        self.order_payment.click_pay_now_master_card()
        # check order is completed
        self.assertTrue(self.order_payment.completed_payment().is_displayed())
        order_number_inorder_payment = self.order_payment.order_number().text
        self.home.click_shopping_cart_window()
        # check shopping cart window is empty
        self.assertTrue(self.shopping_cart_page.shopping_cart_empty().is_displayed())
        self.home.user_emoji_click()
        self.home.click_my_orders()
        print(order_number_inorder_payment)
        print(self.my_orders.order_numbers())
        # check order number is in my orders
        self.assertTrue(order_number_inorder_payment in self.my_orders.order_numbers())

    # Test 10- check login and logout processes
    def test10(self):
        username = 'elad1234'
        password = 'Thbyrby145'
        # log in to site with exist user
        self.home.user_emoji_click()
        self.home.enter_username(username)
        self.home.enter_password(password)
        self.home.sign_in_click()
        # check if the username equals to the text near user item in the top of the page
        self.assertTrue(self.home.check_if_the_use_sign())
        # sign out from site
        self.home.user_emoji_click()
        self.home.click_sign_out()
        # check if user logged out
        self.assertTrue(self.home.check_if_the_use_NOT_sign())














