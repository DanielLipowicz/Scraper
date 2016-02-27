from src.PageObjects import searching_results_page


class MainSearchPage:
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.driver
        self.input_search_by_title = self.driver.find_element_by_id("EQUALS_names")
        self.input_search_by_author = self.driver.find_element_by_id("EQUALS_author")
        self.input_search_by_keywords = self.driver.find_element_by_id("EQUALS_keywords")
        self.combo_search_from_year = self.driver.find_element_by_name("GREATER_EQUAL_published_combo")
        self.combo_search_to_year = self.driver.find_element_by_name("LESS_EQUAL_published_combo")
        self.button_search = self.driver.find_element_by_id("ANY_submitButton")
        self.button_clean = self.driver.find_element_by_id("ANY_resetButton")

    def search_by_keyword(self, keyword):
        self.button_clean.click()
        self.input_search_by_keywords.send_keys(keyword)
        self.button_search.click()
        return searching_results_page.SearchingResultsPage(self.browser)


