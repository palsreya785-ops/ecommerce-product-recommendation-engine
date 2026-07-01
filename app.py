import tkinter as tk
from tkinter import ttk, messagebox
from src.recommendation import RecommendationEngine
from src.utilities import Utilities
from src.report import ReportGenerator
from src.search import SearchEngine

class RecommendationApp:

    def __init__(self, root):

        self.root = root
        self.root.title("E-Commerce Product Recommendation Engine")
        self.root.geometry("1000x650")
        self.root.configure(bg="#ECEFF1")

        self.engine = RecommendationEngine()
        self.search_engine = SearchEngine()

        title = tk.Label(
            root,
            text="🛒 E-Commerce Product Recommendation Engine",
            bg="#1976D2",
            fg="white",
            font=("Arial",20,"bold"),
            pady=12
        )

        title.pack(fill="x")

        top = tk.Frame(root,bg="#ECEFF1")
        top.pack(pady=15)

        tk.Label(top,text="User",bg="#ECEFF1",
                 font=("Arial",11,"bold")).grid(row=0,column=0,padx=5)

        self.user = ttk.Combobox(top,width=18,state="readonly")
        self.user["values"]=Utilities.get_user_ids()
        self.user.current(0)
        self.user.grid(row=0,column=1,padx=5)

        tk.Label(top,text="Search Product",
                 bg="#ECEFF1",
                 font=("Arial",11,"bold")).grid(row=0,column=2,padx=5)

        self.searchBox=tk.Entry(top,width=30)
        self.searchBox.grid(row=0,column=3,padx=5)

        tk.Button(top,
                  text="Search",
                  command=self.search_product,
                  bg="#4CAF50",
                  fg="white").grid(row=0,column=4,padx=5)

        buttonFrame=tk.Frame(root,bg="#ECEFF1")
        buttonFrame.pack()

        buttons=[
            ("Products",self.products),
            ("Recommend",self.recommend),
            ("Generate Report",self.report),
            ("Clear",self.clear),
            ("Exit",root.destroy)
        ]

        c=0
        for text,cmd in buttons:

            tk.Button(buttonFrame,
                      text=text,
                      width=18,
                      command=cmd).grid(row=0,column=c,padx=8,pady=10)

            c+=1

        self.output=tk.Text(root,
                            font=("Consolas",11),
                            width=110,
                            height=25)

        self.output.pack(pady=10)

    def clear(self):

        self.output.delete(1.0,tk.END)

    def products(self):

        self.output.delete(1.0,tk.END)

        self.output.insert(tk.END,
                           "PRODUCT LIST\n")
        self.output.insert(tk.END,
                           "="*90+"\n\n")

        for p in Utilities.get_products():

            self.output.insert(
                tk.END,
                f"{p['product_id']}   "
                f"{p['name']}   "
                f"{p['category']}   "
                f"₹{p['price']}\n"
            )

    def recommend(self):

        self.output.delete(1.0,tk.END)

        user=self.user.get()

        rec=self.engine.recommend(user)

        self.output.insert(
            tk.END,
            f"Recommendations For {user}\n"
        )

        self.output.insert(
            tk.END,
            "="*70+"\n\n"
        )

        for name,score in rec:

            self.output.insert(
                tk.END,
                f"⭐ {name:<35} Score : {score}\n"
            )

    def search_product(self):

        self.output.delete(1.0,tk.END)

        keyword=self.searchBox.get()

        result=self.search_engine.search_by_name(keyword)

        self.output.insert(
            tk.END,
            "SEARCH RESULT\n"
        )

        self.output.insert(
            tk.END,
            "="*80+"\n\n"
        )

        if result.empty:

            self.output.insert(
                tk.END,
                "No Product Found."
            )

            return

        self.output.insert(
            tk.END,
            result.to_string(index=False)
        )

    def report(self):

        user=self.user.get()

        rec=self.engine.recommend(user)

        ReportGenerator.save_report(user,rec)

        messagebox.showinfo(
            "Success",
            "Report Generated Successfully!"
        )

root=tk.Tk()

RecommendationApp(root)

root.mainloop()