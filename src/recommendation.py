from src.similarity import SimilarityEngine
from src.ranking import RankingEngine
from src.priority_queue import PriorityQueueEngine
from src.utilities import Utilities


class RecommendationEngine:

    def __init__(self):

        self.engine = SimilarityEngine()

    def recommend(self, user_id):

        scores = self.engine.calculate_scores(user_id)

        ranked = RankingEngine.rank_products(scores)

        recommendations = PriorityQueueEngine.top_n(ranked, 5)

        final = []

        for product_id, score in recommendations:

            product_name = Utilities.get_product_name(product_id)

            final.append((product_name, score))

        return final