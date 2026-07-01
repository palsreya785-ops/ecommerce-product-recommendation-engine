class RankingEngine:

    @staticmethod
    def rank_products(score_dict):

        ranked = sorted(
            score_dict.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked