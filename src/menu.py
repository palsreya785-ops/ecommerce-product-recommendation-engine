from src.utilities import Utilities
from src.recommendation import RecommendationEngine
from src.report import ReportGenerator


def menu():

    engine = RecommendationEngine()

    while True:

        print("\n")
        print("=" * 55)
        print(" E-Commerce Product Recommendation Engine ")
        print("=" * 55)

        print("1. View Products")
        print("2. View Users")
        print("3. Get Recommendations")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            Utilities.display_products()

        elif choice == "2":

            Utilities.display_users()

        elif choice == "3":

            user = input("Enter User ID : ")

            recommendations = engine.recommend(user)

            print("\nTop Recommendations\n")

            for product, score in recommendations:
                print(f"{product}   Score : {score}")

        elif choice == "4":

            user = input("Enter User ID : ")

            recommendations = engine.recommend(user)

            ReportGenerator.save_report(user, recommendations)

        elif choice == "5":

            print("\nThank you for using the Recommendation Engine!")

            break

        else:

            print("\nInvalid Choice!")