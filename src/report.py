import os


class ReportGenerator:

    @staticmethod
    def save_report(user_id, recommendations):

        os.makedirs("outputs", exist_ok=True)

        filename = "outputs/recommendation_report.txt"

        with open(filename, "w", encoding="utf-8") as file:

            file.write("=" * 50 + "\n")
            file.write(" E-Commerce Recommendation Report\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"User ID : {user_id}\n\n")

            file.write("Recommended Products\n")
            file.write("-" * 40 + "\n")

            for product, score in recommendations:
                file.write(f"{product}    Score : {score}\n")

        print("\n✅ Report saved successfully!")
        print(f"Location : {filename}")