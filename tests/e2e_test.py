
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
import time
from app import launch
import multiprocessing
import os
from unittest import TestCase


def delete_user():
    database_filename = 'info.db'
    connection = sqlite3.connect(database_filename)
    connection.execute(
        "DELETE FROM Users WHERE NAME LIKE ?;", ("e2e",))
    connection.commit()
    connection.close()


class TestConferenceUsers(TestCase):

    @classmethod
    def setUpClass(inst):
        inst.ConferenceAppTest_process=multiprocessing.Process(target=launch,name="ConferenceAppTest",args=('test_info.db',True,))
        inst.ConferenceAppTest_process.start()
        time.sleep(1)
        inst.start = time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        inst.driver = webdriver.Chrome(options = chrome_options)

        #inst.driver.implicitly_wait(1)
        print("Visiting form page")
        inst.driver.get('http://localhost:5000/')


    
    def test_01_add_user(self):
        print("Filling user info")
        name_field = self.driver.find_element(by=By.ID, value='name')
        name_field.send_keys('e2e')
        time.sleep(2)
        phone_field = self.driver.find_element(by=By.ID, value='phone')
        phone_field.send_keys(58456789)
        time.sleep(2)
        email_field = self.driver.find_element(by=By.ID, value='email')
        email_field.send_keys('selenium@gmail.com')
        time.sleep(2)
        job_field = self.driver.find_element(by=By.ID, value='job')
        job_field.send_keys('tester')
        time.sleep(2)

        print("Submitting register form")
        register_button = self.driver.find_element(by=By.ID, value='Submit')
        register_button.click()
        time.sleep(2)
        
        message = self.driver.find_element(by=By.ID, value='message').text
        expected_message = "Thank you for Registering!"

        self.assertIn(expected_message, message)
    
    def test_02_access_list(self):
        print("Clicking view database button")
        view_button = self.driver.find_element(by=By.ID, value='list')
        view_button.click()
        time.sleep(2)
        
        message = self.driver.find_element(by=By.ID, value='database').text
        expected_message = "Database"

        self.assertIn(expected_message, message)

    def test_03_edit_phone(self):
        
        phone_field = self.driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(6) > td:nth-child(3) > form > input[type=text]:nth-child(2)')
        phone_field.send_keys(25)
        time.sleep(2)

        print("Clicking submit button")
        view_button = self.driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(6) > td:nth-child(3) > form > input[type=submit]:nth-child(4)')
        view_button.click()
        time.sleep(2)
        
        message = self.driver.find_element(by=By.ID, value='database').text
        expected_message = "Database"

        self.assertIn(expected_message, message)

    @classmethod
    def tearDownClass(inst):
        inst.end = time.time()
        elapsedtime=inst.end-inst.start
        print("\n-------\nE2E test duration: ", "{:.2f}".format(elapsedtime), "seconds")
        inst.driver.quit()
        delete_user()
        inst.app4test_process.terminate()
        os.remove('test_info.db')
