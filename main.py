from src import Browser

from src.DataOperation import scraping_data_operations
from src.DataOperation import json_open
from src.DataOperation import readed_data_operation

keywords = ["analiza danych", "data warehouse", "hurtownie danych", "analiza ekonometryczna", "ekonometria"]
keywords = ["hurtownie danych", "analiza ekonometryczna",
            "ekonometria"]  # "big data", "data mining", "analiza danych","data warehouse",
Browser = Browser.Browser()
for keyword in keywords:
    print(keyword, ' starts-4')
    scraped = scraping_data_operations.scrap_page(Browser, keyword)
    print(keyword, ' ends')
scraping_data_operations.file_path()
#
# data = json_open.read_json_file("data/ekonometria.json")
# print(type(data))
# print(data.keys())
# print(len(data['publication']))
# readed_data_operation.read_all_publication(data)

print('end')
