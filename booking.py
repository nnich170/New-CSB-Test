import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import subprocess
import time

def close_booking():
    booking.quit()
    booking.destroy()
def open_homepage():
    from open_home import open_homepage
    open_homepage()
def open_home():
    close_booking()
    open_homepage()
def open_promotion():
    from open_promo import open_promo
    open_promo()
def open_the_promopage():
    close_booking()
    open_promotion()

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.append(item)  # Add to the back (end of the list)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front (beginning of the list)
        else:
            return "Queue is empty"
    def peek(self):
        if not self.is_empty():
            return self.items[0]  # View the front element
        else:
            return "Queue is empty"
    def size(self):
        return len(self.items)

queue_tree = None  # Initialize queue_tree as a global variable

def fetch_and_display_queue():
    global queue_tree
    customer_queue = Queue()
    try:
        conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
        cursor = conn.cursor()
        cursor.execute("SELECT *, rowid FROM bookings ORDER BY queue") # Fetch rowid
        result = cursor.fetchall()
        conn.close()
        for row in result:
            customer_queue.enqueue({"Queue": row[3], "Name": row[1], "Phone": row[2], "Promo Type": row[4], "rowid": row[5]}) # Store rowid
        if queue_tree:
            for item in queue_tree.get_children():
                queue_tree.delete(item)
            for item in customer_queue.items:
                queue_tree.insert("", tk.END, values=(item["Queue"], item["Name"], item["Phone"], item["Promo Type"], item["rowid"])) # Display rowid (for debugging)
    except sqlite3.Error as e:
        if queue_tree:
            queue_tree.insert("", tk.END, values=("Error", str(e), "", "", ""))

def remove_selected_customer():
    global queue_tree
    selected_item = queue_tree.selection()
    if not selected_item:
        messagebox.showinfo("Info", "Please select a customer to remove.")
        return

    item_details = queue_tree.item(selected_item[0])['values']
    customer_name = item_details[1]
    customer_rowid = item_details[4] # Get the rowid from the hidden column

    confirm = messagebox.askyesno("Confirm", f"Remove {customer_name} from the queue?")
    if confirm:
        try:
            conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bookings WHERE rowid=?", (customer_rowid,))
            conn.commit()
            conn.close()
            fetch_and_display_queue() # Refresh the queue display
            messagebox.showinfo("Success", f"{customer_name} removed from the queue.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error removing customer: {e}")

def list_box(parent):  # Pass the parent widget (list_frame)
    global queue_tree

    style = ttk.Style()
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    font=("Times New Roman", 12))
    style.configure("Treeview.Heading",
                    background="black",
                    foreground="white",
                    font=("Times New Roman", 12))

    columns = ("Queue", "Name", "Phone", "Promo Type", "ID") # Include ID column
    queue_tree = ttk.Treeview(parent, columns=columns, show="headings", style="Treeview", selectmode=tk.BROWSE) # Enable single selection

    for col in columns:
        queue_tree.heading(col, text=col, anchor=tk.W)
        if col == "ID":
            queue_tree.column(col, width=0, stretch=tk.NO) # Hide the ID column
        else:
            queue_tree.column(col, width=100)

    queue_tree.pack(pady=0, padx=0, fill=tk.BOTH, expand=True) # Remove extra padding

    button_frame = tk.Frame(parent, bg="#D9D9D9") # Frame to hold buttons
    button_frame.pack(pady=5, fill="x")

    refresh_button = tk.Button(button_frame, text="Refresh Queue", bg="#878378", command=fetch_and_display_queue)
    refresh_button.pack(side="left", padx=5)

    remove_button = tk.Button(button_frame, text="Remove", bg="#878378", command=remove_selected_customer)
    remove_button.pack(side="right", padx=5)


def account():
    account_page = "/Users/kanithasem/python test/.vscode/final_project/admin_account.py"
    subprocess.run(["python3", account_page])


def booking_list():
    global booking
    booking = tk.Tk()
    booking.geometry("430x932")
    booking.title("Booking List")
    booking.configure(bg="#D9D9D9")
    #upper brown box

    upper_frame = tk.Frame(booking, width=430, height=80, bg="#878378",relief="ridge", bd=2)
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
    home_btn = tk.Button(upper_frame, text="Home", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_home)
    home_btn.pack(side="left", padx=8, pady=(20, 10))

    promo_btn = tk.Button(upper_frame, text="Promotion", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378", command=open_the_promopage)
    promo_btn.pack(side="left", padx=8, pady=(20, 10))

    booking_btn = tk.Button(upper_frame, text="Booking", font=("Times New Roman", 12, "bold"), fg="black", bg="#878378")
    booking_btn.pack(side="left", padx=8, pady=(20, 10))

    #frame for top-right logo
    def open_account():
        booking.destroy()
        time.sleep(2)
        account()
    logo_frame_2 = tk.Frame(upper_frame, width=50, height=50, bg="white")
    logo_frame_2.pack(side="right", pady=(10, 5), padx=(5, 5))
    acc_btn = tk.Button(logo_frame_2, text="Account", font=("Times New Roman", 12), fg="black", command=open_account)
    acc_btn.pack()


    #image for account (top-right corner)
    try:
        image = Image.open("/Users/kanithasem/python test/.vscode/final_project/image/profilelogo.png")
        photo = ImageTk.PhotoImage(image.resize((40, 60)))

        label_image = tk.Label(logo_frame_2, image=photo, bg="#878378")
        label_image.image = photo
        label_image.pack(fill="both", expand=True)

    except FileNotFoundError:
        tk.Label(logo_frame_2, text="Image not found!", fg="black",bg="#D9D9D9", font=("Arial", 12)).pack()

    tk.Label(booking, text='"Booking List"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(booking, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    # Create a frame to contain the list box
    list_frame = tk.Frame(booking, bg="#D9D9D9")
    list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    list_box(list_frame) # Pass the list_frame to list_box

    down_frame = tk.Frame(booking, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.",
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    booking.mainloop()




# booking_list()


