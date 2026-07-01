import heapq


class PriorityQueueEngine:

    @staticmethod
    def top_n(products, n):

        heap = []

        for product, score in products:
            heapq.heappush(heap, (-score, product))

        result = []

        while heap and len(result) < n:

            score, product = heapq.heappop(heap)

            result.append((product, -score))

        return result