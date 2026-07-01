import pandas as pd
from config import *


class Utilities:

    @staticmethod
    def get_products():
        df = pd.read_csv(PRODUCT_FILE)
        return df.to_dict(orient="records")

    @staticmethod
    def get_user_ids():
        df = pd.read_csv(USER_FILE)
        return df["user_id"].tolist()

    @staticmethod
    def get_product_name(product_id):
        df = pd.read_csv(PRODUCT_FILE)

        result = df[df["product_id"] == product_id]

        if result.empty:
            return product_id

        return result.iloc[0]["name"]

    @staticmethod
    def get_product_category(product_id):
        df = pd.read_csv(PRODUCT_FILE)

        result = df[df["product_id"] == product_id]

        if result.empty:
            return ""

        return result.iloc[0]["category"]

    @staticmethod
    def display_products():

        df = pd.read_csv(PRODUCT_FILE)

        print("\n================ PRODUCT LIST ================\n")

        print(df.to_string(index=False))

    @staticmethod
    def display_users():

        df = pd.read_csv(USER_FILE)

        print("\n================ USER LIST ================\n")

        print(df.to_string(index=False))