import tkinter as tk
from createPass import create_password

# Constants
FONT = ('Rockwell', 12)
RG_COLOR = "#D9D9D9"
GRAY = 'gray'


# set the length of password is 8 by default, or valid value which client enters.
def length_setter():
    pass_len = 8
    try:
        pass_len = int(len_entry.get())
        if pass_len <= 0:
            pass_len = 8
    except:
        pass
    return pass_len


# clear the text of entries and unselect choice boxes.
def flush_widgets():
    len_entry.delete(0, "end")
    password_entry.delete(0, 'end')
    small_chb.deselect()
    capital_chb.deselect()
    digits_chb.deselect()
    punc_chb.deselect()
    copy_text.set('')


# main method which we create password with specific attributes.
def generate_pass():
    is_lower = small_chb_var.get()
    is_upper = capital_chb_var.get()
    is_digits = digits_chb_var.get()
    is_punc = punc_chb_var.get()

    password_length = length_setter()
    password = create_password(password_length, is_upper, is_lower, is_digits, is_punc)

    flush_widgets()

    password_entry.insert(0, password)


# copy the created password to the clipboard.
def copy_pass():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    copy_text.set("Copied to clipboard !")


root = tk.Tk()
root.title("Password Creator")

w, h = 300, 450
# get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(height=False, width=False)

root.iconbitmap('IMG\password_icon.ico')  # Password icon for logo

background_image = tk.PhotoImage(file='IMG\Background.png')  # Space Background
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

copy_image = tk.PhotoImage(file='IMG\icon-copy.png')  # Copy icon
copy_label = tk.Label(root, image=copy_image)

lf = tk.LabelFrame(root, text="Options", fg='white', bg='#020411', width=2000, height=2000)  # Options LF
lf.pack(ipadx=50, padx=30, pady=15, anchor='nw')

small_chb_var = tk.IntVar()
small_chb = tk.Checkbutton(lf, text="Small (abc)", font=FONT, variable=small_chb_var, fg=GRAY, bg='#020411')
small_chb.pack(padx=4, anchor='w')

capital_chb_var = tk.IntVar()
capital_chb = tk.Checkbutton(lf, text="Capital (ABC)", font=FONT, variable=capital_chb_var, fg=GRAY, bg='#020411')
capital_chb.pack(padx=4, anchor='w')

digits_chb_var = tk.IntVar()
digits_chb = tk.Checkbutton(lf, text="Digits (123)", font=FONT, variable=digits_chb_var, fg=GRAY, bg='#020411')
digits_chb.pack(padx=4, anchor='w')

punc_chb_var = tk.IntVar()
punc_chb = tk.Checkbutton(lf, text="Punctuations (!@#)", font=FONT, variable=punc_chb_var, fg=GRAY, bg='#020411')
punc_chb.pack(padx=4, anchor='w')

length_frame = tk.Frame(lf, bg='#020411')
length_frame.pack(anchor='w', pady=5, padx=2)

lenght_label = tk.Label(length_frame, text="Length: (ex:8)      ", font=FONT, fg=GRAY, bg='#020411')
lenght_label.grid(padx=6, row=0, column=0)

len_entry = tk.Entry(length_frame, fg='white', bg='#020411', bd=4, font=FONT, width=7)
len_entry.grid(row=0, column=1, ipady=7, padx=10)

password_frame = tk.LabelFrame(root, text="Password", height=150, width=300, fg='white', bg='#020411')  # Pass LF
password_frame.pack(padx=30, pady=5, ipadx=25)

password_entry = tk.Entry(password_frame, font=FONT, bd=0, bg='#020411', fg='white')
password_entry.grid(row=0, column=0, padx=6, ipady=19)

copy_btn = tk.Button(password_frame, image=copy_image, command=copy_pass, bd=0, width=34, height=40,
                     borderwidth=0, highlightthickness=0)
copy_btn.grid(row=0, column=1, padx=0, pady=0)

generate_btn = tk.Button(root, command=generate_pass, text="Create Password",
                         font=FONT, fg=RG_COLOR, bg='#020411', bd=3)
generate_btn.pack(padx=30, pady=25, ipady=10, ipadx=100)

copy_text = tk.StringVar()
copy_lable = tk.Label(root, text=copy_text, textvariable=copy_text, font=FONT, bg='#020411', fg='green')
copy_lable.pack(pady=0)

root.mainloop()
