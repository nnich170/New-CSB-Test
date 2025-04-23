import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import time

booking_info = []  # List to store database info
checkbox_vars = []  # List to store checkbox variables

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

#create table for customers booking list
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        phonenumber TEXT
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

def booking_page():
    global booking
    booking = tk.Tk()
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
    # Get the selected promotion
    selected_promotion = None
    for idx, promo in enumerate(booking_info):
        if checkbox_vars[idx].get() == 1:  # Check if the checkbox is selected
            selected_promotion = promo
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
        booking.withdraw()
        info = tk.Toplevel()  # Use Toplevel for a popup
        info.geometry("200x150")
        info.title("Congratulation Message")
        tk.Label(info, text=f"Congratulation! \n Your Queue Number is: {queue_number} \n Please fill in the necessary \n info when the registration \n opens to secure your spot.", bg="#D9D9D9", fg="black").pack()
        tk.Button(info, text="Done", command=update_info).pack()
        info.mainloop()
    else:
        messagebox.showerror("Error", "Please select a promotion!")



def update_info():
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
    tk.Label(selection, text="End Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=22)
    tk.Label(selection, text="Amount", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack(side="left", padx=22)

    # Fetch the most recent data from the database
    updated_booking_info = []
    cursor.execute("SELECT * FROM promotions")
    results = cursor.fetchall()
    for row in results:
        updated_booking_info.append({"title": row[2], "startdate": row[4], "enddate": row[5], "amount": row[6]})

    def fill_info():
        booking2.withdraw()
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

        def start_timer():
            #Starts the timer based on the user input.
            limit_time = 60
            timer_display = tk.Label(root1, text="", font=("Arial", 24))
            timer_display.pack(pady=20)
            update_timer(limit_time, timer_display)
        start_timer()

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

            cursor.execute(
                    "INSERT INTO bookings (fullname, phonenumber) VALUES (?, ?)",
                    (full_name, phone_number)
                )
            conn.commit()
            conn.close()

        done_btn = tk.Button(root1, text="Done", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=insert_booking)
        done_btn.pack()

        root1.mainloop()

    # Frame for the Promo Type, start date, etc.
    selection_2 = tk.Frame(booking2, width=200, height=20, relief="solid", bg="#D9D9D9")
    selection_2.pack(fill="x")

    for i in updated_booking_info:
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

        # Create and pack the "Fill" button for this row
        fill_btn = tk.Button(row_frame, text="Fill", font=("Times New Roman", 12), fg="black", bg="#878378", command=fill_info)
        fill_btn.pack(side="left", padx=10)


    # Frame for the select button
    selection3 = tk.Frame(booking2, width=200, height=10, bg="#D9D9D9")
    selection3.pack(pady=20)
    select_btn = tk.Button(selection3, text="Select", font=("Times New Roman", 12, "bold"), bg="#878378", fg="black", command=info_box)
    select_btn.pack()

    # Frame for footer
    down_frame = tk.Frame(booking2, width=430, height=100, bg="#878378", relief="ridge", bd=2)
    down_frame.pack(fill="both", side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    booking2.mainloop()

booking_page()
