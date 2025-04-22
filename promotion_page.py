import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

def open_home_page():
    from start_page import home_page
    home_page()

promotion_items = []

def promotion_page():
    global promotion
    promotion = tk.Tk()
    promotion.geometry("430x932")
    promotion.title("Promotion")
    promotion.configure(bg="#D9D9D9")
    #upper brown box
    upper_frame = tk.Frame(promotion, width=430, height=80, bg="#878378",relief="ridge", bd=2)
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

    tk.Label(promotion, text='"Hot News"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(promotion, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    add_promo_btn = tk.Button(promotion, text="Add Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=promo_info_box)
    add_promo_btn.pack(pady=10)


    down_frame = tk.Frame(promotion, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    promotion.mainloop()


def getfile():
    global filepath
    filepath = filedialog.askopenfilename(title="Select an image File",
                                      filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")])
    if filepath:
        filename_entry.delete(0, tk.END)
        filename_entry.insert(0, filepath)


def promo_info_box():
    global root1, filename_entry, title_entry, description_text, start_date_entry, end_date_entry, amount_entry
    root1 = tk.Toplevel()
    root1.geometry("400x600")
    root1.title("Infobox")
    root1.configure(bg="#D9D9D9")

    tk.Label(root1, text="Please Fill the Info \nBelow to Add Promotion", font=("Times New Roman", 16, "bold"), bg="#D9D9D9", fg="black").pack()
    label_image = tk.Label(root1, text="Image File", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_image.pack(fill="x", padx=10)
    filename_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    filename_entry.pack(fill="x", pady=5, padx=10)

    choose_file_btn = tk.Button(root1, text="Choose File", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=getfile)
    choose_file_btn.pack()

    label_title = tk.Label(root1, text="Promotion Name", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_title.pack(fill="x", padx=10)
    title_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    title_entry.pack(fill="x", pady=5, padx=10)

    label_start_date = tk.Label(root1, text="Start_Date", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_start_date.pack(fill="x", padx=10)
    start_date_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    start_date_entry.pack(fill="x", pady=5, padx=10)

    label_end_date = tk.Label(root1, text="End_Date", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_end_date.pack(fill="x", padx=10)
    end_date_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    end_date_entry.pack(fill="x", pady=5, padx=10)

    label_amount = tk.Label(root1, text="Amount", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_amount.pack(fill="x", padx=10)
    amount_entry = tk.Entry(root1, font=("Times New Roman", 12), bg="#878378", fg="black")
    amount_entry.pack(fill="x", pady=5, padx=10)


    label_description = tk.Label(root1, text="Description", font=("Times New Roman", 12, "bold"), bg="#D9D9D9", fg="black", anchor="w")
    label_description.pack(fill="x", padx=10)
    description_text = tk.Text(root1, width=50, height=10, font=("Times New Roman", 12), bg="#878378", fg="black")
    description_text.pack(fill="x", pady=5, padx=10)


    done_btn = tk.Button(root1, text="Done", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=save_promo_info)
    done_btn.pack()

    root1.mainloop()


def save_promo_info():
    global filepath
    title = title_entry.get()
    description = description_text.get("1.0", "end").strip()  # Get text and remove leading/trailing whitespace
    startdate = start_date_entry.get()
    enddate = end_date_entry.get()
    amount = amount_entry.get()

    if filepath and title and description:
        # Save to the database
        conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS promotions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                start_date TEXT,
                end_date TEXT,
                amount INTEGER
                       
            )''')

        try:
            cursor.execute(
                "INSERT INTO promotions (image_path, title, description, start_date, end_date, amount) VALUES (?, ?, ?, ?, ?, ?)",
                (filepath, title, description, startdate, enddate, amount)
            )
            conn.commit()
            tk.messagebox.showinfo("Success", "Promotion information saved!")
        except sqlite3.Error as e:
            conn.rollback()
            tk.messagebox.showerror("Database Error", f"Error saving to database: {e}")
        finally:
            conn.close()

        promotion_items.append({"image": filepath, "title": title, "description": description, "start_date": startdate, "end_date": enddate, "amount": amount})
        filepath = None  # Reset filepath for the next addition
        root1.destroy()
        update_promo_page()
    else:
        tk.messagebox.showerror("Error", "Please fill all the information.")


def update_promo_page():
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

    add_promo_btn = tk.Button(promotion2, text="Add Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=promo_info_box)
    add_promo_btn.pack(pady=10)

    for item in promotion_items:
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
    description_box.insert(tk.END, f"Start Date: {promo_data['start_date']}\n")
    description_box.insert(tk.END, f"End Date: {promo_data['end_date']}\n")
    description_box.insert(tk.END, f"Amount: {promo_data['amount']}\n")
    description_box.insert(tk.END, f"Details: {promo_data['description']}")
    description_box.config(state=tk.DISABLED) # Make it read-only
    description_box.pack(fill="x", padx=20, pady=(0, 10))

    down_frame = tk.Frame(description_window, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                        font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    description_window.mainloop()

# promotion_page() #function to run 

