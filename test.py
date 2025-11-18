import tkinter as tk
from tkinter import ttk
import pandas as pd


# ---------------------------------------
# CARD CREATOR
# ---------------------------------------
def create_product_card(parent, title, price, rating, reviews, availability):
    style = ttk.Style()
    style.configure("Card.TFrame", background="white", relief="raised", padding=10)
    style.configure("CardTitle.TLabel", font=("Arial", 12, "bold"), background="white")
    style.configure("CardText.TLabel", font=("Arial", 10), background="white")

    card = ttk.Frame(parent, style="Card.TFrame")
    card.pack(fill="x", expand=True, padx=10, pady=10)

    ttk.Label(card, text=title, style="CardTitle.TLabel", wraplength=500)\
        .pack(anchor="w", pady=(0, 10))

    ttk.Label(card, text=f"Price: {price}", style="CardText.TLabel").pack(anchor="w")
    ttk.Label(card, text=f"Rating: {rating}", style="CardText.TLabel").pack(anchor="w")
    ttk.Label(card, text=f"Reviews: {reviews}", style="CardText.TLabel").pack(anchor="w")
    ttk.Label(card, text=f"Availability: {availability}", style="CardText.TLabel")\
        .pack(anchor="w", pady=(0, 5))


# ---------------------------------------
# POP-UP WINDOW TO SHOW ALL PRODUCTS
# ---------------------------------------
def show_all_products():
    df = pd.read_csv("amazon_data.csv")

    popup = tk.Toplevel(root)
    popup.title("All Amazon Products")
    popup.geometry("650x600")

    canvas = tk.Canvas(popup)
    scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)

    scroll_frame = ttk.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for i, row in df.iterrows():
        create_product_card(
            scroll_frame,
            row["title"],
            row["price"],
            row["rating"],
            row["reviews"],
            row["availability"]
        )


# ---------------------------------------
# MAIN WINDOW
# ---------------------------------------
root = tk.Tk()
root.title("Amazon Data Viewer")
root.geometry("400x200")

ttk.Label(root, text="Amazon Scraped Data Viewer", font=("Arial", 14, "bold")).pack(pady=20)

ttk.Button(root, text="Show All Products", command=show_all_products).pack(pady=10)

root.mainloop()
