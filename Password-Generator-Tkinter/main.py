from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random

letters = [*ascii_lowercase, *ascii_uppercase]
digits = [*digits]
symbols = [*punctuation]
all_char = [*letters, *digits, *symbols]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass(char_list: list, entry):
    random.shuffle(char_list)
    pass_len = random.randint(11, 18)
    password = ""
    for i in range(0, pass_len):
        password += random.choice(char_list)
    entry.delete(0, END)
    entry.insert(0, password)
    return


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(entry_web, entry_username, entry_pass):
    website = entry_web.get()
    username = entry_username.get()
    password = entry_pass.get()
    if website and username and password:
        with open(file="./password.txt", mode="a") as file_pass:
            file_pass.writelines(f"{website} | {username} | {password}\n")
    else:
        messagebox.showerror("Erorr", "Incomplete")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry("720x480")
window.resizable(False, False)
window.title("Password Generator")
window.config(pady=80, padx=80)
# window.minsize(width=720, height=480)

canvas = Canvas(window, width=200, height=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(200 / 2, 200 / 2, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(window, text="Website       :", font=("Courier", 12))
website_label.grid(column=0, row=1, sticky='w', pady=5)
username_label = Label(window, text="Email/Username: ", font=("Courier", 12))
username_label.grid(column=0, row=2, sticky='w', pady=5)
pass_label = Label(window, text="Password      : ", font=("Courier", 12))
pass_label.grid(column=0, row=3, sticky='w', pady=5)

website_entry = Entry(window, width=50)
website_entry.grid(column=1, sticky='nws', row=1, pady=5)

username_entry = Entry(window, width=50)
username_entry.grid(column=1, row=2, sticky='nws', pady=5)


pass_entry = Entry(window, width=20, justify="left")
pass_entry.grid(column=1, row=3, sticky='nws', pady=5)


generate_button = Button(window, text="Generate", font=("Courier", 12), command=lambda: generate_pass(all_char,
                                                                                                      pass_entry))
generate_button.grid(column=1, row=3, sticky="E", pady=5)

add_button = Button(window, text="Add", font=("Courier", 12, "bold"), bg="#4D2DB7", command=lambda: save_password(
    entry_web=website_entry,
    entry_pass=pass_entry,
    entry_username=username_entry
))
add_button.grid(column=1, row=4, sticky="ew", pady=5)

window.mainloop()
