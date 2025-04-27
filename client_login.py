import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

def close_homepage():
    home.quit()
    home.destroy()

def promo_page():
    from client_open_promo import open_promo_page
    open_promo_page()

def open_promopage():
    close_homepage()
    promo_page()


database = "/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db"

def create_customers_table():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            phonenumber TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_customers_table()

def insert_customers(fullname, username, phonenumber, password):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO customers (fullname, username, phonenumber, password) VALUES (?, ?, ?, ?)",
            (fullname, username, phonenumber, password)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError as e:
        conn.close()
        if "UNIQUE constraint failed: users.username" in str(e):
            messagebox.showerror("Error", "Username already exists. Please choose another.")
        elif "UNIQUE constraint failed: users.phonenumber" in str(e):
            messagebox.showerror("Error", "Phone number already exists. Please use a different one.")
        else:
            messagebox.showerror("Error", "An error occurred during registration.")
        return False

def validate_login(username, password):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user:
        if user[4] == password:  # Assuming password is the 5th column (index 4)
            return True
        else:
            messagebox.showerror("Error", "Incorrect password.")
            return False
    else:
        messagebox.showerror("Error", "Username not found.")
        return False


def first_page(): #function to run
    global root
    root = tk.Tk()
    root.geometry("430x932")
    root.title("starting page")
    root.configure(bg="#D9D9D9")

    # top brown frame

    upper_frame = tk.Frame(root, width=430, height=80, bg="#878378", relief="ridge")
    upper_frame.pack(side="top")

    # "COFEE CORNER TITLE" (pady use for gap between each row (y-axis), padx use for gap between each column (x-axis))
    tk.Label(root, text="COFFEE", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(pady=20, padx=110, anchor="w")
    tk.Label(root, text="CORNER", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(padx=150, anchor="e")
    image_frame = tk.Frame(root, width=229, height=229, bg="#878378")
    image_frame.pack(pady=30)

    #Using try-exception handling to check if the image availale or not
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((229, 229)))

        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    #Welcome-to-Coffee-Corner-App-for-store-Managers 
    tk.Label(root, text="Welcome to Coffee", fg="black",bg="#D9D9D9",font=("Times New Roman", 20, "bold")).pack()
    tk.Label(root, text="Corner App For", fg="black",bg="#D9D9D9",font=("Times New Roman", 20, "bold")).pack()
    tk.Label(root, text="Customers!", fg="black",bg="#D9D9D9",font=("Times New Roman", 20, "bold")).pack()

    #sign up button
    sign_up_button = tk.Button(root, text="Sign Up", font=("Times New Roman", 15, "bold"), command=open_sign_up)
    sign_up_button.pack(pady=20)

    #log in button
    login_button = tk.Button(root, text="Log In", font=("Times New Roman", 15, "bold"), command=open_log_in)
    login_button.pack(pady=10)

    #text in the quotation
    tk.Label(root, text='"Check the latest promotions from COFFEE CORNER"', fg="black", bg="#D9D9D9", font=("Times New Roman", 15, "italic")).pack(pady=10)
    tk.Label(root, text='and secure your spots"', fg="black", bg="#D9D9D9", font=("Times New Roman", 15, "italic")).pack()
    root.mainloop()
# first_page()

def sign_up():
    global window1
    window1 = tk.Tk()
    window1.geometry("430x932")
    window1.title("sign up")
    window1.configure(bg="#D9D9D9")

    # top brown frame

    upper_frame = tk.Frame(window1, width=430, height=80, bg="#878378")
    upper_frame.pack(side="top")

    # "COFEE CORNER TITLE" (pady use for gap between each row (y-axis), padx use for gap between each column (x-axis))
    tk.Label(window1, text="COFFEE", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(pady=10, padx=110, anchor="w")
    tk.Label(window1, text="CORNER", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(padx=150, anchor="e")
    image_frame = tk.Frame(window1, width=229, height=229, bg="#878378")
    image_frame.pack(pady=(30, 15))

    #Using try-exception handling to check if the image availale or not
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((229, 229)))

        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()
    #sign-up box
    sign_up_frame = tk.Frame(window1, width=340, height=200, bg="#878378", relief="ridge", bd=2, padx=10)
    sign_up_frame.pack(fill="both", padx=20 )

    sign_up = tk.Label(sign_up_frame, text="Sign In", font=("Times New Roman", 20), bg="#878378", fg="black")
    sign_up.pack()

    label_full_name = tk.Label(sign_up_frame, text="Full Name", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_full_name.pack(fill="x")
    full_name_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    full_name_entry.pack(fill="x", pady=5)

    label_user_name = tk.Label(sign_up_frame, text="Username", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_user_name.pack(fill="x")
    user_name_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    user_name_entry.pack(fill="x", pady=2)

    label_phone = tk.Label(sign_up_frame, text="Phone Number", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_phone.pack(fill="x")
    phone_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    phone_entry.pack(fill="x", pady=2)

    label_password = tk.Label(sign_up_frame, text="Password", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_password.pack(fill="x")
    password_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    password_entry.pack(fill="x", pady=2)

    label_password_confirm = tk.Label(sign_up_frame, text="Confirm Password", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_password_confirm.pack(fill="x")
    password_confirm_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    password_confirm_entry.pack(fill="x", pady=(2, 10))

    def register_customer():
        fullname = full_name_entry.get()
        username = user_name_entry.get()
        phonenumber = phone_entry.get()
        password = password_entry.get()
        confirm_password = password_confirm_entry.get()

        if not all([fullname, username, phonenumber, password, confirm_password]):
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if insert_customers(fullname, username, phonenumber, password):
            messagebox.showinfo("Success", "Registration successful!")
            back_client_home()


    #register button
    reg_btn = tk.Button(sign_up_frame, text="Register", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=register_customer)
    reg_btn.pack(pady=(0, 5))

    #frame for the last sentence ("Already have an account")
    down_frame = tk.Frame(window1, bg="#D9D9D9")
    down_frame.pack()
    tk.Label(down_frame, text="Already have an account?", font=("Times New Roman", 16), bg="#D9D9D9", fg="black" ).pack(pady=10, side="left")
    login_btn = tk.Button(down_frame, text="Log In", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_login2)
    login_btn.pack(side="right")

    window1.mainloop()

def login():
    global window2
    window2 = tk.Tk()
    window2.geometry("430x932")
    window2.title("Login")
    window2.configure(bg="#D9D9D9")

    # top brown frame

    upper_frame = tk.Frame(window2, width=430, height=80, bg="#878378")
    upper_frame.pack(side="top")

    # "COFEE CORNER TITLE" (pady use for gap between each row (y-axis), padx use for gap between each column (x-axis))
    tk.Label(window2, text="COFFEE", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(pady=10, padx=110, anchor="w")
    tk.Label(window2, text="CORNER", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(padx=150, anchor="e")
    image_frame = tk.Frame(window2, width=229, height=229, bg="#878378")
    image_frame.pack(pady=30)

    #Using try-exception handling to check if the image availale or not
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((229, 229)))

        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()
    #login box
    login_frame = tk.Frame(window2, width=340, height=200, bg="#878378", relief="ridge", bd=2, padx=20)
    login_frame.pack(fill="both", padx=20 )

    login = tk.Label(login_frame, text="Log In", font=("Times New Roman", 20), bg="#878378", fg="black")
    login.pack(pady=(50, 0))

    label_user_name = tk.Label(login_frame, text="Username", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_user_name.pack(fill="x")
    user_name_entry_login = tk.Entry(login_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    user_name_entry_login.pack(fill="x", pady=2)

    label_phone = tk.Label(login_frame, text="Phone Number", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_phone.pack(fill="x")
    phone_entry = tk.Entry(login_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    phone_entry.pack(fill="x", pady=2)

    label_password = tk.Label(login_frame, text="Password", font=("Times New Roman", 15, "bold"),bg="#878378", fg="black", anchor="w" )
    label_password.pack(fill="x")
    password_entry_login = tk.Entry(login_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    password_entry_login.pack(fill="x", pady=(2, 20))

    def login_user():
        username = user_name_entry_login.get()
        password = password_entry_login.get()
        if validate_login(username, password):
            open_homepage2()
            window2.destroy()
    login_btn = tk.Button(login_frame, text="Log In", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=login_user)
    login_btn.pack(pady=(0, 5))


    #frame for the last sentence ("Create an Account")
    down_frame = tk.Frame(window2, bg="#D9D9D9")
    down_frame.pack(pady=(10, 10))
    tk.Label(down_frame, text="Create an Account?", font=("Times New Roman", 16), bg="#D9D9D9", fg="black" ).pack(pady=10, side="left")
    signup_btn = tk.Button(down_frame, text="Sign Up", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_signup2)
    signup_btn.pack(side="right")

    window2.mainloop()

#to kill the start_page window when users click on the signup button
def open_sign_up():
    root.destroy()
    sign_up()

#to kill the start_page window when users click on the login button
def open_log_in():
    root.destroy()
    login()

#to kill the signup page window when users click on the signup button
def open_login2():
    window1.destroy()
    login()

#to kill the login window when users click on the signup button
def open_signup2():
    window2.destroy()
    sign_up()

def home_page():
    global home
    home = tk.Tk()
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

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_promopage)
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

def open_homepage1():
    window1.destroy()
    home_page()

def open_homepage2():
    window2.destroy()
    home_page()

def back_client_home():
    window1.quit()
    window1.destroy()
    from client_open_promo import open_promo_page
    open_promo_page()


# first_page()










