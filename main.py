from src import Browser
from src.PageObjects import main_search_page

Browser = Browser.Browser()
page = main_search_page.MainSearchPage(Browser)
page = page.search_by_keyword("analiza fundamentalna")
scraped = []
for j in range(page.number_of_results_pages): #range(1):  #
    for i in range(1): #  range(len(page.results)):

        #  create publication_page; scrap publication data; kill publication_page
        publication_page = page.go_to_result_index(i)
        scraped.append(publication_page.create_publication())
        publication_page = None
        page.driver.back()
        page.get_refresh_page_object()
    page = page.go_to_next_result_page()
    page.driver.get_screenshot_as_file('G:/pythonProjekt/Scraper/tmp/screenshot.png')
    page.driver.save_screenshot('G:/pythonProjekt/Scraper/tmp/screenshot.png')
    print('powinno zrobic screena')
for i in range(len(scraped)):
    scraped[i].__repr__()




