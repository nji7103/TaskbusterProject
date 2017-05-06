# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.close()

    def test_it_worked(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Welcome to Django", self.browser.title)

if __name__ == "__main__":
    unittest.main(warnings='ignore')


