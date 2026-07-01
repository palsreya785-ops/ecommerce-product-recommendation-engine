class User:
    """
    Represents an e-commerce user.
    """

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User ID: {self.user_id} | Name: {self.name}"