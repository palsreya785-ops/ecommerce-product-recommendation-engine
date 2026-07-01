class Product:
    """
    Represents a product in the e-commerce store.
    """

    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)

    def __str__(self):
        return (f"ID: {self.product_id} | "
                f"Name: {self.name} | "
                f"Category: {self.category} | "
                f"Price: ₹{self.price:.2f}")