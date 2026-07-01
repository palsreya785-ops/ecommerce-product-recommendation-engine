import pandas as pd
from config import *


class Analytics:

    def __init__(self):

        self.products = pd.read_csv(PRODUCT_FILE)
        self.purchase = pd.read_csv(PURCHASE_FILE)

    def most_purchased_products(self):

        result = (
            self.purchase
            .groupby("product_id")
            .size()
            .sort_values(ascending=False)
        )

        return result

    def category_distribution(self):

        result = (
            self.products
            .groupby("category")
            .size()
            .sort_values(ascending=False)
        )

        return result