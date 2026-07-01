import pandas as pd
from config import *

class DatasetLoader:

    @staticmethod
    def load_products():
        return pd.read_csv(PRODUCT_FILE)

    @staticmethod
    def load_users():
        return pd.read_csv(USER_FILE)

    @staticmethod
    def load_purchase_history():
        return pd.read_csv(PURCHASE_FILE)

    @staticmethod
    def load_search_history():
        return pd.read_csv(SEARCH_FILE)

    @staticmethod
    def load_cart_items():
        return pd.read_csv(CART_FILE)

    @staticmethod
    def load_ratings():
        return pd.read_csv(RATING_FILE)