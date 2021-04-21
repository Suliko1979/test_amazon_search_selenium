from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import random
import random_words
from random_words import RandomWords


class TestAmazon:
    rw = RandomWords()
    search_words = rw.random_words(count=10)

    def setup(self):
        self.driver = webdriver.Chrome(executable_path='F:\django\Selenium lessons\chromedriver.exe')
        self.driver.implicitly_wait(3)
        self.driver.get('https://www.amazon.com/')

    @pytest.mark.parametrize('search_query', search_words)
    def test_search_amazon_dress(self, search_query):
        search= self.driver.find_element_by_id("twotabsearchtextbox")
        search.send_keys(search_query, Keys.ENTER)
        expected = f'\"{search_query}\"'
        actual = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/span/div/span/h1/div/div[1]/div/div'
                                              '/span[3]').text
        assert expected==actual, f'Error'
        self.driver.close()

    def closing_test(self):
        self.driver.quit()
