import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
import sqlite3
import hashlib

# Database setup
def init_db():
    """Initialize the SQLite database and create necessary tables."""
    try:
        conn = sqlite3.connect("coffee_corner.db")
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                full_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        
        # Create client_info table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS client_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization failed: {e}")
    finally:
        conn.close()

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_credentials(username, phone, password):
    """Validate user credentials against the database."""
    try:
        conn = sqlite3.connect("coffee_corner.db")
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute("SELECT * FROM users WHERE username = ? AND phone = ? AND password = ?",
                      (username, phone, hashed_password))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
        return False

def check_user_exists(username, phone):
    """Check if user exists in the database."""
    try:
        conn = sqlite3.connect("coffee_corner.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? OR phone = ?",
                      (username, phone))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
        return False

def first_page():
    global root
    root = tk.Tk()
    root.geometry("430x932")
    root.title("starting page")
    root.configure(bg="#D9D9D9")

    # top brown frame
    upper_frame = tk.Frame(root, width=430, height=80, bg="#878378", relief="ridge")
    upper_frame.pack(side="top")

    # "COFFEE CORNER TITLE"
    tk.Label(root, text="COFFEE", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(pady=20, padx=110, anchor="w")
    tk.Label(root, text="CORNER", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(padx=150, anchor="e")
    image_frame = tk.Frame(root, width=229, height=229, bg="#878378")
    image_frame.pack(pady=30)

    # Image handling
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((229, 229)))
        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    # Welcome text
    tk.Label(root, text="Welcome to Coffee", fg="black", bg="#D9D9D9", font=("Times New Roman", 20, "bold")).pack()
    tk.Label(root, text="Corner Fun For", fg="black", bg="#D9D9D9", font=("Times New Roman", 20, "bold")).pack()
    tk.Label(root, text="Store Managers!", fg="black", bg="#D9D9D9", font=("Times New Roman", 20, "bold")).pack()

    # Buttons
    sign_up_button = tk.Button(root, text="Sign Up", font=("Times New Roman", 15, "bold"), command=open_sign_up)
    sign_up_button.pack(pady=20)
    login_button = tk.Button(root, text="Log In", font=("Times New Roman", 15, "bold"), command=open_log_in)
    login_button.pack(pady=10)

    # Quotation text
    tk.Label(root, text='"Keep your customers updated about', fg="black", bg="#D9D9D9", font=("Times New Roman", 15, "italic")).pack(pady=10)
    tk.Label(root, text='your promotions and track their bookings."', fg="black", bg="#D9D9D9", font=("Times New Roman", 15, "italic")).pack()
    
    root.mainloop()

def sign_up():
    global window1, full_name_entry, user_name_entry, phone_entry, password_entry, password_confirm_entry
    window1 = tk.Tk()
    window1.geometry("430x932")
    window1.title("sign up")
    window1.configure(bg="#D9D9D9")

    # Create a Canvas with a Scrollbar
    canvas = tk.Canvas(window1, bg="#D9D9D9")
    scrollbar = tk.Scrollbar(window1, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#D9D9D9")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the scrollbar and canvas
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Add the scrollable frame to the canvas
    canvas_frame = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Bind the canvas to update the scroll region
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_frame_configure)

    # top brown frame
    upper_frame = tk.Frame(scrollable_frame, width=430, height=80, bg="#878378")
    upper_frame.pack(side="top", fill="x")

    # "COFFEE CORNER TITLE"
    tk.Label(scrollable_frame, text="COFFEE", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(pady=10, padx=110, anchor="w")
    tk.Label(scrollable_frame, text="CORNER", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(padx=150, anchor="e")
    image_frame = tk.Frame(scrollable_frame, width=229, height=229, bg="#878378")
    image_frame.pack(pady=(30, 15))

    # Image handling
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((229, 229)))
        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()
    
    # Sign-up box
    sign_up_frame = tk.Frame(scrollable_frame, width=340, height=400, bg="#878378", relief="ridge", bd=2, padx=10)
    sign_up_frame.pack(fill="x", padx=20, pady=10)

    tk.Label(sign_up_frame, text="Sign Up", font=("Times New Roman", 20), bg="#878378", fg="black").pack(pady=10)

    # Entry fields
    label_full_name = tk.Label(sign_up_frame, text="Full Name", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_full_name.pack(fill="x")
    full_name_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    full_name_entry.pack(fill="x", pady=5)

    label_user_name = tk.Label(sign_up_frame, text="Username", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_user_name.pack(fill="x")
    user_name_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    user_name_entry.pack(fill="x", pady=5)

    label_phone = tk.Label(sign_up_frame, text="Phone Number", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_phone.pack(fill="x")
    phone_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    phone_entry.pack(fill="x", pady=5)

    label_password = tk.Label(sign_up_frame, text="Password", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_password.pack(fill="x")
    password_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid", show="*")
    password_entry.pack(fill="x", pady=5)

    label_password_confirm = tk.Label(sign_up_frame, text="Confirm Password", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_password_confirm.pack(fill="x")
    password_confirm_entry = tk.Entry(sign_up_frame, font=("Times New Roman", 12), bg="#878378", relief="solid", show="*")
    password_confirm_entry.pack(fill="x", pady=5)

    # Register button
    reg_btn = tk.Button(sign_up_frame, text="Register", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=validate_and_register)
    reg_btn.pack(pady=10)

    # Already have an account
    down_frame = tk.Frame(scrollable_frame, bg="#D9D9D9")
    down_frame.pack(fill="x", pady=10)
    tk.Label(down_frame, text="Already have an account?", font=("Times New Roman", 16), bg="#D9D9D9", fg="black").pack(side="left", padx=10)
    login_btn = tk.Button(down_frame, text="Log In", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_login2)
    login_btn.pack(side="right", padx=10)

    # Ensure the canvas can be scrolled with the mouse wheel
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    window1.mainloop()

def login():
    global window2, user_name_entry, phone_entry, password_entry
    window2 = tk.Tk()
    window2.geometry("430x932")
    window2.title("Login")
    window2.configure(bg="#D9D9D9")

    # Create a Canvas with a Scrollbar
    canvas = tk.Canvas(window2, bg="#D9D9D9")
    scrollbar = tk.Scrollbar(window2, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#D9D9D9")

    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas_frame = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_frame_configure)

    # top brown frame
    upper_frame = tk.Frame(scrollable_frame, width=430, height=80, bg="#878378")
    upper_frame.pack(side="top", fill="x")

    # "COFFEE CORNER TITLE"
    tk.Label(scrollable_frame, text="COFFEE", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(pady=10, padx=110, anchor="w")
    tk.Label(scrollable_frame, text="CORNER", fg="black", bg="#D9D9D9", font=("Times New Roman", 30, "bold")).pack(padx=150, anchor="e")
    image_frame = tk.Frame(scrollable_frame, width=229, height=229, bg="#878378")
    image_frame.pack(pady=30)

    # Image handling
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((229, 229)))
        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()
    
    # Login box
    login_frame = tk.Frame(scrollable_frame, width=340, height=300, bg="#878378", relief="ridge", bd=2, padx=20)
    login_frame.pack(fill="x", padx=20, pady=10)

    tk.Label(login_frame, text="Log In", font=("Times New Roman", 20), bg="#878378", fg="black").pack(pady=10)

    label_user_name = tk.Label(login_frame, text="Username", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_user_name.pack(fill="x")
    user_name_entry = tk.Entry(login_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    user_name_entry.pack(fill="x", pady=5)

    label_phone = tk.Label(login_frame, text="Phone Number", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_phone.pack(fill="x")
    phone_entry = tk.Entry(login_frame, font=("Times New Roman", 12), bg="#878378", relief="solid")
    phone_entry.pack(fill="x", pady=5)

    label_password = tk.Label(login_frame, text="Password", font=("Times New Roman", 15, "bold"), bg="#878378", fg="black", anchor="w")
    label_password.pack(fill="x")
    password_entry = tk.Entry(login_frame, font=("Times New Roman", 12), bg="#878378", relief="solid", show="*")
    password_entry.pack(fill="x", pady=5)

    login_btn = tk.Button(login_frame, text="Log In", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=validate_login)
    login_btn.pack(pady=10)

    # Create an account
    down_frame = tk.Frame(scrollable_frame, bg="#D9D9D9")
    down_frame.pack(fill="x", pady=10)
    tk.Label(down_frame, text="Create an Account?", font=("Times New Roman", 16), bg="#D9D9D9", fg="black").pack(side="left", padx=10)
    signup_btn = tk.Button(down_frame, text="Sign Up", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_signup2)
    signup_btn.pack(side="right", padx=10)

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    window2.mainloop()

def open_sign_up():
    root.destroy()
    sign_up()

def open_log_in():
    root.destroy()
    login()

def open_login2():
    window1.destroy()
    login()

def open_signup2():
    window2.destroy()
    sign_up()

def home_page():
    global home
    home = tk.Tk()
    home.geometry("430x932")
    home.title("Home")
    home.configure(bg="#D9D9D9")

    # Create a Canvas with a Scrollbar
    canvas = tk.Canvas(home, bg="#D9D9D9")
    scrollbar = tk.Scrollbar(home, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#D9D9D9")

    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas_frame = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_frame_configure)

    # Upper brown box
    upper_frame = tk.Frame(scrollable_frame, width=430, height=80, bg="#878378", relief="ridge", bd=2)
    upper_frame.pack(fill="x", side="top")

    # Coffee corner logo
    logo_frame_1 = tk.Frame(upper_frame, width=79, height=79, bg="white")
    logo_frame_1.pack(side="left", pady=(10, 5))

    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/cornerlogo.png")
        photo = ImageTk.PhotoImage(image.resize((79, 79)))
        label_image = tk.Label(logo_frame_1, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(logo_frame_1, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    # Navigation buttons
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    home_btn.pack(side="left", padx=8, pady=(20, 10))
    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_promotion_page)
    promo_btn.pack(side="left", padx=8, pady=(20, 10))
    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    # Profile logo
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))

    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))
        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    # Coffee shop image
    image_frame = tk.Frame(scrollable_frame, width=300, height=200, bg="white")
    image_frame.pack(pady=(20, 5))
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/coffeecorner.png")
        photo = ImageTk.PhotoImage(image.resize((300, 200)))
        label_image = tk.Label(image_frame, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()

    # Welcome and about us
    tk.Label(scrollable_frame, text="Welcome", font=("Times New Roman", 30, "bold"), fg="black", bg="#D9D9D9").pack()
    tk.Label(scrollable_frame, text="_______________________", font=("Times New Roman", 10, "bold"), fg="black", bg="#D9D9D9").pack(pady=(0, 10))
    tk.Label(scrollable_frame, text="About Us", font=("Times New Roman", 24, "bold"), fg="black", bg="#D9D9D9").pack(pady=(0, 10))
    tk.Label(scrollable_frame, 
             text="Welcome to COFFEE CORNER, a leading coffee shop in Cambodia. \n While our commitment to exceptional coffee remains paramount,\n we pride ourselves on offering our client different kinds of drinks \nwith affordable price to brighten their day. Over the past two years, \nCOFFEE CORNER has proudly received significant support from our \nvalued customers, establishing a strong reputation for quality and \nservice within the Cambodian market.", 
             font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()
    
    # Small logos
    small_logo_frame = tk.Frame(scrollable_frame, width=430, height=60, bg="#D9D9D9", bd=2)
    small_logo_frame.pack(pady=20, fill="x")

    image1_frame = tk.Frame(small_logo_frame, width=60, height=60, bg="#D9D9D9")
    image1_frame.pack(side="left", padx=(50, 60))
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/coffeeimage.png")
        photo = ImageTk.PhotoImage(image.resize((60, 60)))
        label_image = tk.Label(image1_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image1_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()
    tk.Label(image1_frame, text="Exceptional", font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()

    image2_frame = tk.Frame(small_logo_frame, width=60, height=60, bg="#D9D9D9")
    image2_frame.pack(side="left", padx=(0, 50))
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/thumb.png")
        photo = ImageTk.PhotoImage(image.resize((60, 60)))
        label_image = tk.Label(image2_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image2_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()
    tk.Label(image2_frame, text="Fresh", font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()

    image3_frame = tk.Frame(small_logo_frame, width=60, height=60, bg="#D9D9D9")
    image3_frame.pack(side="left", padx=(10, 50))
    try:
        image = Image.open("/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/image/wallet.png")
        photo = ImageTk.PhotoImage(image.resize((60, 60)))
        label_image = tk.Label(image3_frame, image=photo, bg="#D9D9D9")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)
    except FileNotFoundError:
        tk.Label(image3_frame, text="Image not found!", fg="black", bg="#D9D9D9", font=("Arial", 12)).pack()
    tk.Label(image3_frame, text="Affordable", font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack()

    tk.Label(scrollable_frame, text='"Come and taste the difference at \nCOFFEE CORNER!!!!"', font=("Times New Roman", 18, "bold"), fg="black", bg="#D9D9D9").pack(pady=10)
    
    down_frame = tk.Frame(scrollable_frame, width=430, height=100, bg="#878378", relief="ridge", bd=2)
    down_frame.pack(fill="x", side="bottom")
    tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.", 
             font=("Times New Roman", 12), fg="black", bg="#878378").pack()

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    home.mainloop()

def open_homepage1():
    window1.destroy()
    home_page()

def open_homepage2():
    window2.destroy()
    home_page()

def open_promotion_page():
    promotion_page_client = "/Users/dethsokunboranich/IdeaProjects/Final Project CSB/CSB Final/New-CSB-Test/client_open_promo.py"
    try:
        subprocess.run(["python3", promotion_page_client])
    except FileNotFoundError:
        messagebox.showerror("Error", "Promotion page script (client_open_promo.py) not found. Please ensure the file exists in the correct directory.")
    except subprocess.SubprocessError as e:
        messagebox.showerror("Error", f"Failed to open promotion page: {e}")

def validate_login():
    username = user_name_entry.get().strip()
    phone = phone_entry.get().strip()
    password = password_entry.get().strip()

    if not all([username, phone, password]):
        messagebox.showwarning("Incomplete Information", "Please fill out all fields to log in.")
        return

    if not check_user_exists(username, phone):
        messagebox.showerror("No Account", "No account found with these credentials. Please register first.")
        open_signup2()
        return

    if validate_credentials(username, phone, password):
        open_homepage2()
    else:
        messagebox.showerror("Login Failed", "Invalid username, phone number, or password.")

def validate_and_register():
    full_name = full_name_entry.get().strip()
    username = user_name_entry.get().strip()
    phone = phone_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = password_confirm_entry.get().strip()

    if not all([full_name, username, phone, password, confirm_password]):
        messagebox.showwarning("Incomplete Information", "Please fill out all fields before registering.")
        return
    if password != confirm_password:
        messagebox.showerror("Password Mismatch", "Passwords do not match.")
        return
    if not phone.isdigit() or len(phone) < 8:
        messagebox.showerror("Invalid Phone", "Phone number must be numeric and at least 8 digits.")
        return

    # Check if user already exists
    if check_user_exists(username, phone):
        messagebox.showerror("Registration Failed", "Username or phone number already exists. Please log in instead.")
        open_login2()
        return

    try:
        conn = sqlite3.connect("coffee_corner.db")
        cursor = conn.cursor()
        
        # Insert into users table
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (full_name, username, phone, password) VALUES (?, ?, ?, ?)",
                      (full_name, username, phone, hashed_password))
        
        # Insert into client_info table
        cursor.execute("INSERT INTO client_info (full_name, username, phone) VALUES (?, ?, ?)",
                      (full_name, username, phone))
        
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Registration successful! You can now log in.")
        open_homepage1()

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")

# Initialize the database and start the app
init_db()
first_page()
