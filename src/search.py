import pandas as pd
from config import *


class SearchEngine:

    def __init__(self):

        self.products = pd.read_csv(PRODUCT_FILE)

    def search_by_name(self, keyword):

        keyword = keyword.lower()

        return self.products[
            self.products["name"].str.lower().str.contains(keyword)
        ]

    def search_by_category(self, category):

        return self.products[
            self.products["category"].str.lower() == category.lower()
        ]