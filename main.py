from src import Browser
from src.PageObjects import main_search_page
import json
import os

Browser = Browser.Browser()
page = main_search_page.MainSearchPage(Browser)
page = page.search_by_keyword("analiza fundamentalna")
scraped = []
json_file = []
for j in range(2):# range(page.number_of_results_pages): # range(1):  #
    for i in range(1): #  range(len(page.results)):
        #  create publication_page; scrap publication data; kill publication_page
        publication_page = page.go_to_result_index(i)
        scraped.append(publication_page.create_publication())
        publication_page = None
        page.driver.back()
        page.get_refresh_page_object()
    page = page.go_to_next_result_page()
print(scraped)
print('pobrano dane ')
for i in range(len(scraped)):
    json_file.append(json.dumps(scraped[i].__dict__))
    print (json_file)
 # os.pathrealpath(__file__)) represent script file path
fileName = os.path.dirname(os.path.realpath(__file__))+'scrapedData2.json'
print(fileName)
file = open(fileName, 'w')
for JSON in json_file:
    file.writelines(JSON)
    print(JSON)
file.close()



