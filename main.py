from src import Browser

from src.DataOperation import data_operations

Browser = Browser.Browser()
scraped = data_operations.scrap_page(Browser)
data_operations.save_to_file(scraped)
# data_operations.file_path()

