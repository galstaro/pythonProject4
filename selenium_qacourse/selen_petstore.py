from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import petstore_classes


def test_price_randomproducts(driver,numberofproducts):
    count=0
    for i in range(numberofproducts):
        # pick category
        c=petstore_classes.Category_Page(driver)
        c.category()
        c.choose_category_randomly()
        # pick product
        p=petstore_classes.Products_Page(driver)
        p.product_id()
        p.choose_product_randomly()
        # pick item
        items=petstore_classes.Items_Page(driver)
        items.item_id()
        items.choose_item_randomly()
        # add to cart item
        item=petstore_classes.Item_Page(driver)
        item.add_to_cart()
        item.click_add_to_cart()
        # change quantity of item
        shop=petstore_classes.Shopping_Cart_Page(driver)
        shop.item_line()
        shop.quantity()
        quantity_number=shop.enter_random_quantity()
        # update cart
        shop.update_cart()
        shop.click_update_cart()
        # test if list price of item multiply the quantity of it equal to the total price
        if shop.list_price()*quantity_number == shop.total_price():
            count+=shop.total_price()
            print(f"test {i+1}-total price: passed")
        else:
            count += shop.total_price()
            print(f"test {i+1}-total price: failed")
        sleep(2)
        # back to home page
        if i!=numberofproducts-1:
            shop.back_link()
            shop.click_back_link()
    # test if all total prices combined equal to the subtotal price
    count=round(count,2)
    if count == shop.subtotal_price():
        print("test -subtotal amount: passed")


service = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.maximize_window()
driver.implicitly_wait(10)
test_price_randomproducts(driver,3)
driver.close()