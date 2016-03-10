from src import Browser

from src.DataOperation import data_operations

keywords = ["big data", "data mining", "analiza danych", "data warehouse", "hurtownie danych", "analiza ekonometryczna",
            "ekonometria"]
Browser = Browser.Browser()
for keyword in keywords:
    scraped = data_operations.scrap_page(Browser, keyword)
    data_operations.save_to_file(scraped, keyword)
    print(keyword)
# data_operations.file_path()

