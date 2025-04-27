# account_page.py
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

database = "/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db"
logged_in_user_id = None  # Initialize logged_in_user_id

def get_customers_details(user_id):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT fullname, username, phonenumber FROM customers WHERE id=?", (user_id,))
    user_details = cursor.fetchone()
    conn.close()
    return user_details

def create_account_page(master):
    global account_window
    account_window = tk.Toplevel(master)
    account_window.geometry("430x932")
    account_window.title("Account Setting")
    account_window.configure(bg="#D9D9D9")

    upper_frame = tk.Frame(account_window, width=430, height=80, bg="#878378")
    upper_frame.pack(side="top", fill="x")


    tk.Label(upper_frame, text="Account Setting", font=("Times New Roman", 20, "bold"), bg="#878378", fg="black").pack(pady=15)

    if logged_in_user_id is not None:
        user_info = get_customers_details(logged_in_user_id)
        if user_info:
            fullname = user_info[0]
            username = user_info[1]
            phone = user_info[2]

            # Profile icon frame
            profile_frame = tk.Frame(account_window, bg="#D9D9D9")
            profile_frame.pack(pady=20)
            try:
                profile_image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png") # Adjust path as needed
                profile_photo = ImageTk.PhotoImage(profile_image.resize((100, 100)))
                profile_label = tk.Label(profile_frame, image=profile_photo, bg="#D9D9D9")
                profile_label.image = profile_photo
                profile_label.pack()
            except FileNotFoundError:
                tk.Label(profile_frame, text="Profile Icon", font=("Times New Roman", 16), bg="#D9D9D9").pack()

            tk.Label(account_window, text=fullname, font=("Times New Roman", 18, "bold"), bg="#D9D9D9", fg="black").pack()
            tk.Label(account_window, text=f"@{username}", font=("Times New Roman", 14), bg="#D9D9D9", fg="black").pack(pady=5)

            # Personal Info frame
            info_frame = tk.Frame(account_window, bg="#878378", padx=20, pady=20)
            info_frame.pack(pady=20, padx=20, fill="x")
            tk.Label(info_frame, text="Personal Info", font=("Times New Roman", 16, "bold"), bg="#F0F0F0", anchor="w", fg="black").pack(fill="x", pady=(0, 10))
            tk.Label(info_frame, text=f"Phone: {phone}", font=("Times New Roman", 12), bg="#F0F0F0", anchor="w", fg="black").pack(fill="x", pady=5)
            tk.Label(info_frame, text="Bio", font=("Times New Roman", 12), bg="#F0F0F0", anchor="w", fg="black").pack(fill="x", pady=5)
            tk.Text(info_frame, font=("Times New Roman", 14), bg="#F0F0F0", height=10, fg="black").pack(fill="x", pady=2) # Replace with actual bio if stored


            # Connect with us section
            connect_frame = tk.Frame(account_window, bg="#878378")
            connect_frame.pack(side="bottom", fill="x", pady=10)
            tk.Label(connect_frame, text="Connect with us on:", font=("Times New Roman", 12), bg="#878378", fg="black").pack()
            tk.Label(connect_frame, text="Facebook: Coffee Corner", font=("Times New Roman", 12), bg="#878378", fg="black").pack()
            tk.Label(connect_frame, text="Tel: (+855)77 481 111", font=("Times New Roman", 12), bg="#878378", fg="black").pack()
            tk.Label(connect_frame, text="Location: Phnom Penh, Cambodia.", font=("Times New Roman", 12), bg="#878378", fg="black").pack()
        else:
            tk.Label(account_window, text="Could not retrieve user information.", font=("Times New Roman", 16), bg="#D9D9D9").pack(pady=20)
    else:
        tk.Label(account_window, text="No user logged in.", font=("Times New Roman", 16), bg="#D9D9D9").pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("")
    # Simulate a logged-in user for testing
    logged_in_user_id = 1
    create_account_page(root)
    root.mainloop()

