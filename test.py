import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from variables import *
import os

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", "./chromedriver")


class Test001(unittest.TestCase):
    # This method check procedure of adding item to the cart
    def test_add_to_shopping_cart(self) -> None:
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        search_field = driver.find_element(By.NAME, "search")
        search_field.send_keys(item)
        search_field.send_keys(Keys.RETURN)
        add_to_cart = driver.find_element(
            By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]'
        )
        add_to_cart.click()
        check_cart = driver.find_element(By.LINK_TEXT, "Shopping Cart")
        check_cart.click()
        self.assertTrue(item_assertion in driver.page_source)
        driver.__exit__()

    def test_delete_from_shopping_cart(self) -> None:
        #  This method check procedure of deleting item from the cart
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        search_field = driver.find_element(By.NAME, "search")
        search_field.send_keys(item)
        search_field.send_keys(Keys.RETURN)
        add_to_cart = driver.find_element(
            By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]'
        )
        add_to_cart.click()
        check_cart = driver.find_element(By.LINK_TEXT, "Shopping Cart")
        check_cart.click()
        self.assertTrue(item_assertion in driver.page_source)
        delete_from_cart = driver.find_element(
            By.XPATH,
            '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]',
        )
        delete_from_cart.click()
        driver.refresh()
        self.assertTrue(delete_assertion in driver.page_source)
        driver.__exit__()

    def test_my_account_register(self) -> None:
        # This method check procedure of sign in to webpage
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        my_account_button = driver.find_element(By.LINK_TEXT, "My Account")
        my_account_button.click()
        register_button = driver.find_element(By.LINK_TEXT, "Register")
        register_button.click()
        input_name = driver.find_element(By.NAME, "firstname")
        input_name.click()
        input_name.send_keys(username)
        input_last_name = driver.find_element(By.NAME, "lastname")
        input_last_name.click()
        input_last_name.send_keys(lastname)
        input_email = driver.find_element(By.NAME, "email")
        input_email.click()
        input_email.send_keys(email)
        input_tel = driver.find_element(By.NAME, "telephone")
        input_tel.click()
        input_tel.send_keys(phone)
        input_password = driver.find_element(By.NAME, "password")
        input_password.click()
        input_password.send_keys(password)
        input_password_confirm = driver.find_element(By.NAME, "confirm")
        input_password_confirm.click()
        input_password_confirm.send_keys(password)
        input_agree = driver.find_element(By.NAME, "agree")
        input_agree.click()
        continue_button = driver.find_element(
            By.CSS_SELECTOR, 'input[value="Continue"]'
        )
        continue_button.click()
        driver.__exit__()

    def test_login(self) -> None:
        # This method check procedure of log in to webpage
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        my_account_button = driver.find_element(By.LINK_TEXT, "My Account")
        my_account_button.click()
        login_button = driver.find_element(By.LINK_TEXT, "Login")
        login_button.click()
        email_field = driver.find_element(By.NAME, "email")
        email_field.click()
        email_field.send_keys(email)
        password_field = driver.find_element(By.NAME, "password")
        password_field.click()
        password_field.send_keys(password)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        submit_button.click()
        self.assertTrue("My Account" in driver.page_source)

    def test_broken_links_main_page(self) -> None:
        # This method examine webpage to find broken links
        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        driver.implicitly_wait(15)
        links = driver.find_elements(By.CSS_SELECTOR, "a")
        res = dict()
        for link in links:
            r = requests.head(link.get_attribute("href"))
            res[link.get_attribute("href")] = r.status_code
            with open('broken_links.txt', 'w') as f:
                print("{:<8} {:<15}".format('Link', 'Status code'), file=f)
                for key, value in res.items():
                    if value > 299:
                        print("{:<8} {:<15}".format(key, value), file=f)
        driver.__exit__()
