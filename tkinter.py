import tkinter as tk

base = tk.Tk()
base.geometry('500x500')

# Title section
base.title("registration form")

# Create the label
lbl0 = tk.Label(base, text="Registration form")
lbl0.place(x=80, y=60)
#name
lbl1 = tk.Label(base, text="Name")
lbl1.place(x=80, y=100)

#textbox
entry1=tk.Entry(base)
entry1.place(x=150,y=100)

#contact
lbl2 = tk.Label(base, text="Contact")
lbl2.place(x=80, y=140)

entry2 = tk.Entry(base)
entry2.place(x=150, y=140)


#gender
lbl3 = tk.Label(base, text="Gender")
lbl3.place(x=80, y=180)


gender = tk.StringVar()
radio1 = tk.Radiobutton(base, text="Male", variable=gender, value="Male")
radio1.place(x=150, y=180)
radio2 = tk.Radiobutton(base, text="Female", variable=gender, value="Female")
radio2.place(x=150, y=210)

# Hobbies label and checkboxes
lbl4 = tk.Label(base, text="Hobbies")
lbl4.place(x=80, y=250)

hobby1 = tk.BooleanVar()
#checkbox
check1 = tk.Checkbutton(base, text="Reading", variable=hobby1)
check1.place(x=150, y=250)

hobby2 = tk.BooleanVar()
check2 = tk.Checkbutton(base, text="Traveling", variable=hobby2)
check2.place(x=150, y=280)
hobby3 = tk.BooleanVar()
check3 = tk.Checkbutton(base, text="Sports", variable=hobby3)
check3.place(x=150, y=310)
#submit
submit_button = tk.Button(base, text="Submit")
submit_button.place(x=200, y=350)

