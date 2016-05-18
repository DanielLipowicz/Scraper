from src import Browser

from src.DataOperation import scraping_data_operations
from src.DataOperation import json_open
from src.DataOperation import readed_data_operation

#
# scraper
#


def scrap_data():
    keywords = ["analiza danych", "data warehouse", "hurtownie danych", "analiza ekonometryczna", "ekonometria"]
    keywords = ["big data", "hurtownie danych", "analiza ekonometryczna",
                "ekonometria"]  # "data mining", "analiza danych","data warehouse",
    browser = Browser.Browser()
    for keyword in keywords:
        print(keyword, ' starts-4')
        scraped = scraping_data_operations.scrap_page(browser, keyword)
        print(keyword, ' ends')
    scraping_data_operations.file_path()

scrap_data()
# scraper end
#

# data = json_open.read_json_file("data/ekonometria.json")
# print(type(data))
# print(data.keys())
# print(len(data['publication']))
# readed_data_operation.read_all_publication(data)

print('end')
