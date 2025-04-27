import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import subprocess

def close_promopage():
    promotion2.destroy()

def open_homepage():
    from open_clienthome import homepage
    homepage()

def open_home_page():
    close_promopage()
    open_homepage()

def bookingpage():
    from client_booking import booking_page
    booking_page()

def open_booking():
    close_promopage()
    bookingpage()


promotion_info = []

def update_promo_page():
    global promotion2
    promotion2 = tk.Tk()
    promotion2.geometry("430x932")
    promotion2.title("Promotion")
    promotion2.configure(bg="#D9D9D9")

    #upper brown box
    upper_frame = tk.Frame(promotion2, width=430, height=80, bg="#878378",relief="ridge", bd=2)
    upper_frame.pack(fill="both",side="top")
    #frame for coffee corner logo (top-left corner logo)
    logo_frame_1 = tk.Frame(upper_frame, width=79, height=79, bg="white")
    logo_frame_1.pack(side="left", pady=(10, 5))

    #image for coffee corner logo
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((79, 79)))

        label_image = tk.Label(logo_frame_1, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_1, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #the 3 upper logos
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_home_page)
    home_btn.pack(side="left", padx=8, pady=(20, 10))

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    promo_btn.pack(side="left", padx=8, pady=(20, 10))

    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    #frame for top-right logo
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))

    #image for account (top-right corner)
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))

        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    tk.Label(promotion2, text='"Hot News"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(promotion2, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()


    conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promotions")
    results = cursor.fetchall()
    for row in results:
        promotion_info.append({"image": row[1], "title": row[2], "startdate": row[4], "enddate": row[5], "amount": row[6], "description": row[3]})
    
    for item in promotion_info:
        create_promo_display(promotion2, item)

    down_frame = tk.Frame(promotion2, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                        font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    promotion2.mainloop()

def create_promo_display(parent, promo_item):

    image_frame = tk.Frame(parent, width=150, height=200, bg="#D9D9D9")
    image_frame.pack(pady=10)
    try:
        image = Image.open(promo_item["image"])  # Open the image file
        photo = ImageTk.PhotoImage(image.resize((150, 150)))  # Create a PhotoImage object
        label_image = tk.Label(image_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo  # Keep a reference to avoid garbage collection
        label_image.pack(fill="both", expand=True)

        tk.Label(image_frame, text="Promotion Name", fg="black", font=("Times New Roman", 14, "bold"), bg="#D9D9D9").pack(pady=5)
        tk.Label(image_frame, width=50,text=promo_item["title"], fg="black", font=("Times New Roman", 15, "bold"), bg="#D9D9D9").pack(padx=(150, 150))


        description_btn = tk.Button(image_frame, text="Description", font=("Times New Roman", 10), fg="black", bg="#878378",
                                     command=lambda item=promo_item: description_page(item))
        description_btn.pack(pady=5)

    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black", bg="pink", font=("Arial", 12)).pack()

def description_page(promo_data):
    description_window = tk.Toplevel()
    description_window.geometry("430x932")
    description_window.title("Description")
    description_window.configure(bg="#D9D9D9")
    #upper brown box
    upper_frame = tk.Frame(description_window, width=430, height=80, bg="#878378",relief="ridge", bd=2)
    upper_frame.pack(fill="both",side="top")
    #frame for coffee corner logo (top-left corner logo)
    logo_frame_1 = tk.Frame(upper_frame, width=79, height=79, bg="white")
    logo_frame_1.pack(side="left", pady=(10, 5))

    #image for coffee corner logo
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((79, 79)))

        label_image = tk.Label(logo_frame_1, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_1, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #the 3 upper logos
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_home_page)
    home_btn.pack(side="left", padx=8, pady=(20, 10))

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    promo_btn.pack(side="left", padx=8, pady=(20, 10))

    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    #frame for top-right logo
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))

    #image for account (top-right corner)
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))

        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    back_btn_frame = tk.Frame(description_window, width=430, height=30, bg="#D9D9D9")
    back_btn_frame.pack(anchor="w", padx=10, pady=10)
    back_btn = tk.Button(back_btn_frame, text="Back", font=("Times New Roman", 12), bg="#878378", fg="black", command=description_window.destroy)
    back_btn.pack(side="left")

    tk.Label(description_window, text='"Description"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(description_window, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    promo_image_frame = tk.Frame(description_window, width=300, height=200, bg="#D9D9D9")
    promo_image_frame.pack(pady=10)

    try:
        image = Image.open(promo_data["image"])
        photo = ImageTk.PhotoImage(image.resize((300, 200)))
        promo_label = tk.Label(promo_image_frame, image=photo, bg="#D9D9D9")
        promo_label.image = photo
        promo_label.pack()
    except FileNotFoundError:
        tk.Label(promo_image_frame, text="Image not found!", fg="black", bg="pink", font=("Arial", 12)).pack()

    description_box = tk.Text(description_window, font=("Times New Roman", 12), bg="white", fg="black", height=10, width=200, relief="solid")
    description_box.insert(tk.END, f"Title: {promo_data['title']}\n")
    description_box.insert(tk.END, f"Start Date: {promo_data['startdate']}\n")
    description_box.insert(tk.END, f"End Date: {promo_data['enddate']}\n")
    description_box.insert(tk.END, f"Amount: {promo_data['amount']}\n")
    description_box.insert(tk.END, f"Details: {promo_data['description']}")
    description_box.config(state=tk.DISABLED) # Make it read-only
    description_box.pack(fill="x", padx=20, pady=(0, 10))

    book_btn = tk.Button(description_window, text="Book Now", fg="black", bg="#878378", font=("Times New Roman", 12), command=open_booking)
    book_btn.pack()

    down_frame = tk.Frame(description_window, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                        font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    description_window.mainloop()


# update_promo_page()


