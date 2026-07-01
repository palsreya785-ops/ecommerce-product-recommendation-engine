import pandas as pd
from collections import defaultdict
from config import *


class SimilarityEngine:

    def __init__(self):

        self.products = pd.read_csv(PRODUCT_FILE)
        self.purchase = pd.read_csv(PURCHASE_FILE)
        self.search = pd.read_csv(SEARCH_FILE)
        self.cart = pd.read_csv(CART_FILE)
        self.ratings = pd.read_csv(RATING_FILE)

    def calculate_scores(self, user_id):

        scores = defaultdict(float)

        purchased = set(
            self.purchase[self.purchase.user_id == user_id]["product_id"]
        )

        searched = list(
            self.search[self.search.user_id == user_id]["product_id"]
        )

        cart = list(
            self.cart[self.cart.user_id == user_id]["product_id"]
        )

        rated = self.ratings[self.ratings.user_id == user_id]

        # Search History
        for pid in searched:

            category = self.products.loc[
                self.products.product_id == pid,
                "category"
            ].values[0]

            similar = self.products[
                self.products.category == category
            ]

            for _, row in similar.iterrows():

                if row.product_id not in purchased:

                    scores[row.product_id] += 3

        # Cart Items
        for pid in cart:

            category = self.products.loc[
                self.products.product_id == pid,
                "category"
            ].values[0]

            similar = self.products[
                self.products.category == category
            ]

            for _, row in similar.iterrows():

                if row.product_id not in purchased:

                    scores[row.product_id] += 5

        # Ratings
        for _, row in rated.iterrows():

            if row.rating >= 4:

                category = self.products.loc[
                    self.products.product_id == row.product_id,
                    "category"
                ].values[0]

                similar = self.products[
                    self.products.category == category
                ]

                for _, p in similar.iterrows():

                    if p.product_id not in purchased:

                        scores[p.product_id] += row.rating

        # Cold Start
        if len(scores) == 0:

            popular = (
                self.purchase
                .groupby("product_id")
                .size()
                .sort_values(ascending=False)
            )

            for pid in popular.index:

                scores[pid] += 2

        return scores