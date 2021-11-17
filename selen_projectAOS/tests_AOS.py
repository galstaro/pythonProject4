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
        self.sheet.add_pass_or_fail(1,total_items== int(number_of_items))
        self.assertEqual(total_items, int(number_of_items))

    def test2(self):
        qu=[]
        co=[]
        names=[]
        price=[]
        for i in range(3):
            self.home.click_category(2, i + 1)
            self.category.click_product(2, i + 1)
            quantity = self.product.enter_quantity(2, i + 1)
            qu.append(quantity)
            color=self.product.choose_color(2,i+1)
            co.append(color)
            product_name=self.product.product_name()
            names.append(product_name)
            pr=self.product.price()
            price.append(float(pr))
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        names.reverse()
        self.assertListEqual(names,self.home.names_in_cart())
        qu.reverse()
        self.assertListEqual(qu,self.home.quantities_in_cart())
        co.reverse()
        price.reverse()
        print(co)
        print(self.home.colors_in_cart())
        exept_price = 0.0
        for i in range(3):
            exept_price += qu[i] * price[i]
        self.assertListEqual(self.home.colors_in_cart(),co)
        self.sheet.add_pass_or_fail(2, round(exept_price,2) == self.home.price())
        self.assertEqual(round(exept_price,2),self.home.price())

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
        self.assertEqual(number_of_products,number_products_after_remove+1)

    def test4(self):
        self.home.click_category(4, 1)
        self.category.click_product(4, 1)
        self.product.click_add_to_cart()
        self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        text=self.shopping_cart_page.title_text_shopping_cart()
        self.sheet.add_pass_or_fail(4, text=='SHOPPING CART')
        self.assertEqual(text,'SHOPPING CART')

    def test5(self):
        qu = []
        names = []
        price = []
        for i in range(3):
            self.home.click_category(5,i + 1)
            self.category.click_product(5,i+1)
            quantity = self.product.enter_quantity(5,i+1)
            qu.append(quantity)
            product_name = self.product.product_name()
            names.append(product_name)
            pr = self.product.price()
            price.append(float(pr))
            print(f"name: {product_name}, quantity: {quantity}, price: {float(pr)}")
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        total_price=self.shopping_cart_page.price()
        exept_price=0.0
        for i in range(3):
            exept_price += qu[i] * price[i]
        print(exept_price,total_price)
        total_price=float(total_price)
        total_price=round(total_price,2)
        self.sheet.add_pass_or_fail(5, round(exept_price,2) == total_price)
        self.assertEqual(round(exept_price,2),total_price)

    def test6(self):
        for i in range(3):
            self.home.click_category(6, i + 1)
            self.category.click_product(6, i + 1)
            self.product.enter_quantity(6,i+1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        edits=self.shopping_cart_page.edit()
        before_change_quantities=self.shopping_cart_page.quantities_in_cart()
        for x in range(len(edits)):
            edits=self.shopping_cart_page.edit()
            edits[x].click()
            self.product.change_quantity()
            self.product.click_add_to_cart()
            self.home.click_shopping_cart_window()
            sleep(10)
        pass_or_fail=True
        after_change_quantities = self.shopping_cart_page.quantities_in_cart()
        print(before_change_quantities)
        print(after_change_quantities)
        for i in range(len(after_change_quantities)):
            if before_change_quantities[i]==after_change_quantities[i]:
                pass_or_fail=False
                break
        self.sheet.add_pass_or_fail(6,pass_or_fail)
        self.assertTrue(pass_or_fail)

    def test7(self):
        self.home.click_category(7,1)
        self.category.click_product(7,1)
        self.driver.back()
        self.assertEqual(self.category.category_title(),"TABLETS")
        self.driver.back()
        self.assertEqual(self.home.text_in_home(),"SPECIAL OFFER")
        self.sheet.add_pass_or_fail(7,self.home.text_in_home()=="SPECIAL OFFER")

    def test8(self):
        for i in range(3):
            self.home.click_category(8, i + 1)
            self.category.click_product(8, i + 1)
            self.product.enter_quantity(8, i + 1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        self.shopping_cart_page.click_checkout()
        self.order_payment.click_registration()
        self.create_account.enter_username()
        self.create_account.enter_email()
        self.create_account.enter_password()
        self.create_account.enter_confirm_password()
        self.wait.until(EC.visibility_of_element_located((By.NAME, "i_agree")))
        self.create_account.click_conditions_of_use_agreement()
        self.wait.until(EC.element_to_be_clickable((By.ID,"register_btnundefined")))
        self.create_account.click_register()
        self.order_payment.click_next()
        self.wait.until(EC.visibility_of_element_located((By.NAME, "safepay_username")))
        self.order_payment.enter_safe_pay_username()
        self.order_payment.enter_safe_pay_password()
        self.order_payment.click_pay_now()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")))
        self.assertTrue(self.order_payment.completed_payment().is_displayed())
        self.home.click_shopping_cart_window()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")))
        self.sheet.add_pass_or_fail(8, self.shopping_cart_page.shopping_cart_empty().is_displayed())
        self.assertTrue(self.shopping_cart_page.shopping_cart_empty().is_displayed())
        tracking_number_inorder_payment=self.order_payment.tracking_number().text
        self.home.user_emoji_click()
        self.home.click_my_orders()
        self.assertTrue(tracking_number_inorder_payment in self.my_orders.tracking_numbers())



    def test9(self):
        for i in range(3):
            self.home.click_category(9,i+1)
            self.category.click_product(9,i+1)
            self.product.enter_quantity(9,i+1)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        self.home.click_checkout()
        self.order_payment.enter_username("elad1234")
        self.order_payment.enter_password("Thbyrby145")
        self.order_payment.click_login()
        self.order_payment.click_next()
        self.order_payment.click_master_credit()
        self.order_payment.click_edit()
        self.order_payment.fill_master_card_details("123456789123","432", "elad-ratner", "2", "4")
        self.order_payment.click_pay_now_master_card()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")))
        self.assertTrue(self.order_payment.completed_payment().is_displayed())
        tracking_number_inorder_payment = self.order_payment.tracking_number().text
        self.home.click_shopping_cart_window()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")))
        self.sheet.add_pass_or_fail(9, self.shopping_cart_page.shopping_cart_empty().is_displayed())
        self.assertTrue(self.shopping_cart_page.shopping_cart_empty().is_displayed())
        self.home.user_emoji_click()
        self.home.click_my_orders()
        self.assertTrue(tracking_number_inorder_payment in self.my_orders.tracking_numbers())














