import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import time
import subprocess


booking_info = []  # List to store database info
checkbox_vars = []  # List to store checkbox variables
fill_buttons = []  # List to store fill buttons

# Initialize database connection
conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
cursor = conn.cursor()

# Create table for queue number if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS queue_number (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    current_queue INTEGER
)
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        phonenumber TEXT,
        queue INTEGER,
        promo TEXT
    )
    """)

# Initialize queue number in the database if not already set
cursor.execute("SELECT current_queue FROM queue_number ORDER BY id DESC LIMIT 1")
result = cursor.fetchone()
if result is None:
    cursor.execute("INSERT INTO queue_number (current_queue) VALUES (0)")
    conn.commit()

def get_current_queue():
    """Retrieve the current queue number from the database."""
    cursor.execute("SELECT current_queue FROM queue_number ORDER BY id DESC LIMIT 1")
    return cursor.fetchone()[0]

def increment_queue():
    """Increment the queue number in the database."""
    current_queue = get_current_queue()
    new_queue = current_queue + 1
    cursor.execute("INSERT INTO queue_number (current_queue) VALUES (?)", (new_queue,))
    conn.commit()
    return new_queue

def bookingpaging():
    description_window2.quit()
    description_window2.destroy()
    from open_client_booking import openbooking
    openbooking()

def openhomepage():
    info2.destroy()
    home_page()

def open_accountpage():
    account = "/Users/kanithasem/python test/.vscode/final_project/client_account.py"
    subprocess.run(["python3", account])


def home_page():
    booking.withdraw()
    global home
    home = tk.Toplevel()
    home.geometry("430x932")
    home.title("Login")
    home.configure(bg="#D9D9D9")

    #upper brown box

    upper_frame = tk.Frame(home, width=430, height=80, bg="#878378",relief="ridge", bd=2)
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
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    home_btn.pack(side="left", padx=8, pady=(20, 10))

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=promopage)
    promo_btn.pack(side="left", padx=8, pady=(20, 10))

    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    #frame for top-right logo
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))
    account_btn = tk.Button(logo_frame_2, text="Account", font=("Times New Roman", 12), fg="black", bg="#878378", command=open_accountpage)
    account_btn.pack()

    #image for account (top-right corner)
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))

        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #Coffee Corner shop frame and its image
    image_frame = tk.Frame(home, width=300, height=200, bg="white" )
    image_frame.pack(pady=(20, 5))
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/coffeecorner.png")
        photo = ImageTk.PhotoImage(image.resize((300, 200)))

        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #welcome and about us info
    tk.Label(home, text="Welcome", font=("Times New Roman", 30, "bold"), fg="black", bg="#D9D9D9").pack()
    tk.Label(home, text="_______________________", font=("Times New Roman", 10, "bold"), fg="black", bg="#D9D9D9").pack(pady=(0, 10))
    tk.Label(home, text="About Us", font=("Times New Roman", 24, "bold"), fg="black", bg="#D9D9D9").pack(pady=(0, 10))
    tk.Label(home, 
             text="Welcome to COFFEE CORNER, a leading coffee shop in Cambodia. \n While our commitment to exceptional coffee remains paramount,\n we pride ourselves on offering our client different kinds of drinks \nwith affordable price to brighten their day. Over the past two years, \nCOFFEE CORNER has proudly received significant support from our \nvalued customers, establishing a strong reputation for quality and \nservice within the Cambodian market.", 
             font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()
    
    #image under About us info
    small_logo_frame = tk.Frame(home, width=430, height=60, bg="#D9D9D9", bd=2)
    small_logo_frame.pack(pady=20, fill="both")

    #frame for coffee image under about us
    image1_frame = tk.Frame(small_logo_frame, width=60, height=60, bg="#D9D9D9")
    image1_frame.pack(side="left", padx=(50, 60))

    #cup of coffee image
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/coffeeimage.png")
        photo = ImageTk.PhotoImage(image.resize((60, 60)))

        label_image = tk.Label(image1_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image1_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #text under cup of coffee image
    tk.Label(image1_frame, text="Exceptional", font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()

    #frame and image for thumb image
    image2_frame = tk.Frame(small_logo_frame, width=60, height=60, bg="#D9D9D9")
    image2_frame.pack(side="left", padx=(0, 50))

    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/thumb.png")
        photo = ImageTk.PhotoImage(image.resize((60, 60)))

        label_image = tk.Label(image2_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image2_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #text under the thumb up image
    tk.Label(image2_frame, text="Fresh", font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()


    image3_frame = tk.Frame(small_logo_frame, width=60, height=60, bg="#D9D9D9")
    image3_frame.pack(side="left", padx=(10, 50))
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/wallet.png")
        photo = ImageTk.PhotoImage(image.resize((60, 60)))

        label_image = tk.Label(image3_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image3_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    tk.Label(image3_frame, text="Affordable", font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()

    tk.Label(home, text='"Come and taste the difference at \nCOFFEE CORNER!!!!"', font=("Times New Roman", 18, "bold"), fg="black", bg="#D9D9D9").pack(pady=10)
    

    down_frame = tk.Frame(home, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.", 
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()
    
    home.mainloop()

# promotion_info = []
def promopage():
    promotion_info = []
    home.withdraw()
    global promotion2
    promotion2 = tk.Toplevel()
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
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
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
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
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

    book_btn = tk.Button(description_window, text="Book Now", fg="black", bg="#878378", font=("Times New Roman", 12), command=bookingpaging)
    book_btn.pack()

    down_frame = tk.Frame(description_window, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                        font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    description_window.mainloop()


def promopage2():
    root1.withdraw()
    promotion_info2 = []
    global promotion3
    promotion3 = tk.Toplevel()
    promotion3.geometry("430x932")
    promotion3.title("Promotion")
    promotion3.configure(bg="#D9D9D9")

    #upper brown box
    upper_frame = tk.Frame(promotion3, width=430, height=80, bg="#878378",relief="ridge", bd=2)
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
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
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

    tk.Label(promotion3, text='"Hot News"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(promotion3, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()


    conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promotions")
    results = cursor.fetchall()
    for row in results:
        promotion_info2.append({"image": row[1], "title": row[2], "startdate": row[4], "enddate": row[5], "amount": row[6], "description": row[3]})
    
    for item in promotion_info2:
        create_promo_display2(promotion3, item)

    down_frame = tk.Frame(promotion3, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                        font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    promotion3.mainloop()

def create_promo_display2(parent, promo_item):

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
                                     command=lambda item=promo_item: description_page2(item))
        description_btn.pack(pady=5)

    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black", bg="pink", font=("Arial", 12)).pack()

def description_page2(promo_data):
    global description_window2
    description_window2 = tk.Toplevel()
    description_window2.geometry("430x932")
    description_window2.title("Description")
    description_window2.configure(bg="#D9D9D9")
    #upper brown box
    upper_frame = tk.Frame(description_window2, width=430, height=80, bg="#878378",relief="ridge", bd=2)
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
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
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

    back_btn_frame = tk.Frame(description_window2, width=430, height=30, bg="#D9D9D9")
    back_btn_frame.pack(anchor="w", padx=10, pady=10)
    back_btn = tk.Button(back_btn_frame, text="Back", font=("Times New Roman", 12), bg="#878378", fg="black", command=description_window2.destroy)
    back_btn.pack(side="left")

    tk.Label(description_window2, text='"Description"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(description_window2, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    promo_image_frame = tk.Frame(description_window2, width=300, height=200, bg="#D9D9D9")
    promo_image_frame.pack(pady=10)

    try:
        image = Image.open(promo_data["image"])
        photo = ImageTk.PhotoImage(image.resize((300, 200)))
        promo_label = tk.Label(promo_image_frame, image=photo, bg="#D9D9D9")
        promo_label.image = photo
        promo_label.pack()
    except FileNotFoundError:
        tk.Label(promo_image_frame, text="Image not found!", fg="black", bg="pink", font=("Arial", 12)).pack()

    description_box = tk.Text(description_window2, font=("Times New Roman", 12), bg="white", fg="black", height=10, width=200, relief="solid")
    description_box.insert(tk.END, f"Title: {promo_data['title']}\n")
    description_box.insert(tk.END, f"Start Date: {promo_data['startdate']}\n")
    description_box.insert(tk.END, f"End Date: {promo_data['enddate']}\n")
    description_box.insert(tk.END, f"Amount: {promo_data['amount']}\n")
    description_box.insert(tk.END, f"Details: {promo_data['description']}")
    description_box.config(state=tk.DISABLED) # Make it read-only
    description_box.pack(fill="x", padx=20, pady=(0, 10))

    book_btn = tk.Button(description_window2, text="Book Now", fg="black", bg="#878378", font=("Times New Roman", 12), command=bookingpaging)
    book_btn.pack()

    down_frame = tk.Frame(description_window2, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                        font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    description_window2.mainloop()

def booking_page():
    global booking
    booking = tk.Toplevel()
    booking.geometry("430x932")
    booking.title("Promotion")
    booking.configure(bg="#D9D9D9")

    # Upper brown box
    upper_frame = tk.Frame(booking, width=430, height=80, bg="#878378", relief="ridge", bd=2)
    upper_frame.pack(fill="both", side="top")

    # Frame for coffee corner logo (top-left corner logo)
    logo_frame_1 = tk.Frame(upper_frame, width=79, height=79, bg="white")
    logo_frame_1.pack(side="left", pady=(10, 5))

    # Image for coffee corner logo
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((79, 79)))

        label_image = tk.Label(logo_frame_1, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_1, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    # The 3 upper logos
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=home_page)
    home_btn.pack(side="left", padx=8, pady=(20, 10))

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    promo_btn.pack(side="left", padx=8, pady=(20, 10))

    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    # Frame for top-right logo
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))

    # Image for account (top-right corner)
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))

        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    tk.Label(booking, text='"Booking"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(booking, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    selection = tk.Frame(booking, width=200, height=10, relief="solid", bg="#D9D9D9")
    selection.pack(fill="x")

    tk.Label(selection, text="Promo Type", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=10)
    tk.Label(selection, text="Start Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=22)
    tk.Label(selection, text="End Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=22)
    tk.Label(selection, text="Amount", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=22)

    # Fetch data from database and append into the list to display
    cursor.execute("SELECT * FROM promotions")
    results = cursor.fetchall()
    for row in results:
        booking_info.append({"title": row[2], "startdate": row[4], "enddate": row[5], "amount": row[6]})

    # Frame for the Promo Type, start date, etc.
    selection_2 = tk.Frame(booking, width=200, height=20, relief="solid", bg="#D9D9D9")
    selection_2.pack(fill="x")

    for i in booking_info:
        row_frame = tk.Frame(selection_2, bg="#D9D9D9")  # Create a frame for each row
        row_frame.pack(fill="x", pady=5)

        # Create a Checkbutton
        checkbox_var = tk.IntVar()
        checkbox_vars.append(checkbox_var)  # Variable to store the state of the checkbox
        tk.Checkbutton(row_frame, variable=checkbox_var, font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left")

        # Create a Label next to the Checkbutton
        tk.Label(row_frame, text=i["title"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left")
        tk.Label(row_frame, text=i["startdate"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=20)
        tk.Label(row_frame, text=i["enddate"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=20)
        tk.Label(row_frame, text=i["amount"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=20)

    # Frame for the select button
    selection3 = tk.Frame(booking, width=200, height=10, bg="#D9D9D9")
    selection3.pack(pady=20)
    select_btn = tk.Button(selection3, text="Select", font=("Times New Roman", 12, "bold"), bg="#878378", fg="black", command=info_box)
    select_btn.pack()

    # Frame for footer
    down_frame = tk.Frame(booking, width=430, height=100, bg="#878378", relief="ridge", bd=2)
    down_frame.pack(fill="both", side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    booking.mainloop()

def info_box():
    global selected_promotion
    # Get the selected promotion
    selected_promotion = None
    selected_index = -1
    for idx, promo in enumerate(booking_info):
        if checkbox_vars[idx].get() == 1:  # Check if the checkbox is selected
            selected_promotion = promo
            selected_index = idx
            break

    if selected_promotion:
        # Increment the queue number
        queue_number = increment_queue()

        # Decrement the amount in the database
        cursor.execute(
            "UPDATE promotions SET amount = amount - 1 WHERE title = ?",
            (selected_promotion["title"],)
        )
        conn.commit()  # Save changes to the database

        # Show the queue number to the client
        global info
        # booking.quit()
        booking.withdraw()
        info = tk.Toplevel()  # Use Toplevel for a popup
        info.geometry("200x150")
        info.title("Congratulation Message")
        tk.Label(info, text=f"Congratulation! \n Your Queue Number is: {queue_number}\n for {selected_promotion["title"]} \n Please fill in the necessary \n info when the registration \n opens to secure your spot.", bg="#D9D9D9", fg="black").pack()
        tk.Button(info, text="Done", command=lambda: update_info(selected_index)).pack() # Pass the index
        info.mainloop()
    else:
        messagebox.showerror("Error", "Please select a promotion!")

def fill_info():
    booking2.destroy()
    global root1
    root1 = tk.Tk()
    root1.geometry("400x300")
    root1.title("Infobox")
    root1.configure(bg="#D9D9D9")

    def update_timer(remaining_time, label):
    # Updates the timer label with the remaining time.
        if remaining_time >= 0:
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            seconds = remaining_time % 60
            label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            root1.after(1000, update_timer, remaining_time - 1, label) # Schedule update every 1 second
        else:
            label.config(text="Time's up!")
            tk.messagebox.showinfo("Time's Up", "Please Try Again.")
            promopage2()
            
    def start_timer():
        #Starts the timer based on the user input.
        limit_time = 60
        timer_display = tk.Label(root1, text="", font=("Arial", 24))
        timer_display.pack(pady=20)
        update_timer(limit_time, timer_display)
    start_timer()

    queue_label = tk.Label(root1, text=get_current_queue(), font=("Times New Roman", 16, "bold"), bg="#D9D9D9", fg="black")
    queue_label.pack()
    tk.Label(root1, text="Please Fill the Info \nBelow to Secure Your Spot", font=("Times New Roman", 16, "bold"), bg="#D9D9D9", fg="black").pack()
    label_image = tk.Label(root1, text="Full Name", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_image.pack(fill="x", padx=10)
    fullname_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    fullname_entry.pack(fill="x", pady=5, padx=10)

    phone_number = tk.Label(root1, text="Phone Number", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    phone_number.pack(fill="x", padx=10)
    phone_number_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    phone_number_entry.pack(fill="x", pady=5, padx=10)

    def insert_booking():
        full_name = fullname_entry.get()
        phone_number = phone_number_entry.get()
        queue = get_current_queue()
        promo_type = selected_promotion['title']

        cursor.execute(
                "INSERT INTO bookings (fullname, phonenumber, queue, promo) VALUES (?, ?, ?, ?)",
                (full_name, phone_number, queue, promo_type)
            )
        conn.commit()
        conn.close()
        
        booking.withdraw()
        global info2
        info2 = tk.Toplevel()  # Use Toplevel for a popup
        info2.geometry("200x150")
        info2.title("Congratulation Message")
        tk.Label(info2, text=f"Congratulation! \n You have secure a spot \nfor our promotion. \n Please comes at pick up \nyour gifts.", bg="#D9D9D9", fg="black").pack()
        tk.Button(info2, text="Done", command=openhomepage).pack() # Close the info box
        info2.mainloop()
        

    done_btn = tk.Button(root1, text="Done", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=insert_booking)
    done_btn.pack()
    root1.mainloop()
def update_info(selected_index):
    global booking2
    time.sleep(5)  # Simulate a delay (optional)
    info.destroy()
    booking2 = tk.Toplevel()
    booking2.geometry("430x932")
    booking2.title("Fill Info")
    booking2.configure(bg="#D9D9D9")

    upper_frame = tk.Frame(booking2, width=430, height=80, bg="#878378", relief="ridge", bd=2)
    upper_frame.pack(fill="both", side="top")

    # Frame for coffee corner logo (top-left corner logo)
    logo_frame_1 = tk.Frame(upper_frame, width=79, height=79, bg="white")
    logo_frame_1.pack(side="left", pady=(10, 5))

    # Image for coffee corner logo
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((79, 79)))

        label_image = tk.Label(logo_frame_1, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_1, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    # The 3 upper logos
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    home_btn.pack(side="left", padx=8, pady=(20, 10))

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    promo_btn.pack(side="left", padx=8, pady=(20, 10))

    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    # Frame for top-right logo
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))

    # Image for account (top-right corner)
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))

        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    tk.Label(booking2, text='"Booking"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(booking2, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    selection = tk.Frame(booking2, width=200, height=10, relief="solid", bg="#D9D9D9")
    selection.pack(fill="x")

    tk.Label(selection, text="Promo Type", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=10)
    tk.Label(selection, text="Start Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=22)
    tk.Label(selection, text="End Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=25)
    tk.Label(selection, text="Amount", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=25)

    # Fetch the most recent data from the database
    updated_booking_info = []
    cursor.execute("SELECT * FROM promotions")
    results = cursor.fetchall()
    for row in results:
        updated_booking_info.append({"title": row[2], "startdate": row[4], "enddate": row[5], "amount": row[6]})

    # Frame for the Promo Type, start date, etc.
    selection_2 = tk.Frame(booking2, width=200, height=20, relief="solid", bg="#D9D9D9")
    selection_2.pack(fill="x")

    for idx, i in enumerate(updated_booking_info):
        row_frame = tk.Frame(selection_2, bg="#D9D9D9")  # Create a frame for each row
        row_frame.pack(fill="x", pady=5)

        # Create a Label for the promo info
        tk.Label(row_frame, text=i["title"], font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=10)
        tk.Label(row_frame, text=i["startdate"], font=("Times New Roman", 12), fg="black",bg="#D9D9D9").pack(side="left", padx=25) 
        tk.Label(row_frame, text=i["enddate"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=25)
        tk.Label(row_frame, text=i["amount"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=25)

        if idx == selected_index:
            fill_btn = tk.Button(row_frame, text="Fill", font=("Times New Roman", 12), fg="black", bg="#878378", command=fill_info)
            fill_btn.pack(side="left", padx=10)

    # Frame for footer
    down_frame = tk.Frame(booking2, width=430, height=100, bg="#878378", relief="ridge", bd=2)
    down_frame.pack(fill="both", side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    booking2.mainloop()

# booking_page()



