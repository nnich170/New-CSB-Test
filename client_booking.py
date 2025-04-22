import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

booking_info = [] #list to store database info
def booking_page():
    booking = tk.Tk()
    booking.geometry("430x932")
    booking.title("Promotion")
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

    tk.Label(booking, text='"Booking"', font=("Times New Roman", 20, "bold"), fg="black", bg="#D9D9D9").pack(pady=(10, 0))
    tk.Label(booking, text='____________________', font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9").pack()

    selection = tk.Frame(booking, width=200, height=10, relief="solid", bg="#D9D9D9")
    selection.pack(fill="x")

    tk.Label(selection, text="Promo Type", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9" ).pack(side="left", padx=10)
    tk.Label(selection, text="Start Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9" ).pack(side="left", padx=22)
    tk.Label(selection, text="End Date", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9" ).pack(side="left", padx=22)
    tk.Label(selection, text="Amount", font=("Times New Roman", 12, "bold"), fg="black", bg="#D9D9D9" ).pack(side="left", padx=22)

    #fetch data from database and append into the list to display
    conn = sqlite3.connect("/Users/kanithasem/python test/.vscode/final_project/cornercoffee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promotions")
    results = cursor.fetchall()
    for row in results: 
        booking_info.append({"title": row[2], "startdate": row[4], "enddate": row[5], "amount": row[6]})

    #frame for the Promo Tyoe, start date.. line
    selection_2 = tk.Frame(booking, width=200, height=10, relief="solid", bg="#D9D9D9")
    selection_2.pack(fill="x")

    for i in booking_info:
        row_frame = tk.Frame(selection_2, bg="#D9D9D9")  # Create a frame for each row
        row_frame.pack(fill="x", pady=5)

        # Create a Checkbutton
        checkbox_var = tk.IntVar()  # Variable to store the state of the checkbox
        tk.Checkbutton(row_frame, variable=checkbox_var, font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left")

        # Create a Label next to the Checkbutton
        tk.Label(row_frame, text=i["title"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left")
        tk.Label(row_frame, text=i["startdate"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=20)
        tk.Label(row_frame, text=i["enddate"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=20)
        tk.Label(row_frame, text=i["amount"], font=("Times New Roman", 12), fg="black", bg="#D9D9D9").pack(side="left", padx=20)

    #frame for the select button
    selection3 = tk.Frame(booking, width=200, height=10, bg="#D9D9D9")
    selection3.pack(pady=20)
    select_btn = tk.Button(selection3, text="Select", font=("Times New Roman", 12, "bold"), bg="#878378", fg="black")
    select_btn.pack()


    #frame for footer
    down_frame = tk.Frame(booking, width=430, height=100, bg="#878378",relief="ridge", bd=2)
    down_frame.pack(fill="both",side="bottom")
    down_label = tk.Label(down_frame, text="Connect with us on \n Facebook: Coffee Corner \nTel: (+855)77 481 111 \nLocation: Phnom Penh, Cambodia.", 
                          font=("Times New Roman", 12), fg="black", bg="#878378")
    down_label.pack()

    booking.mainloop()

booking_page()


