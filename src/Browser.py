from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Browser:
    def __init__(self):
        #  ### in case when phantom JS is not installed
        self.driver = webdriver.Firefox()
        self.bazekonURL = "http://bazekon.icm.edu.pl/bazekon/search/article.action"
        # ### in case when phantomJS is installed
        # self.driver = webdriver.Phantomjs()

        self.reset_waiting_time()
        self.driver.set_window_position(960, 0, windowHandle='current')
        self.driver.set_window_size(960, 1040, windowHandle='current')
        self.Select = Select

    def __del__(self):

        self.driver.close()

    def get_sarching_page(self):
        self.driver.get(self.bazekonURL)

    def set_wait_time(self, time):
        self.driver.implicitly_wait(time)

    def reset_waiting_time(self):
        self.driver.implicitly_wait(30)

