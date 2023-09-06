from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass(entry_password: Entry):
    letters = [*ascii_lowercase, *ascii_uppercase]
    numbers = [*digits]
    symbols = [*punctuation]

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)
    return


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(entry_web: Entry, entry_username: Entry, entry_pass: Entry):
    website = entry_web.get()
    username = entry_username.get()
    password = entry_pass.get()
    if website and username and password:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are details entered:\n Email/Username: {username}\n "
                                               f"Password: {password}\n its ok to save?")
        if is_ok:
            with open(file="./password.txt", mode="a") as file_pass:
                file_pass.writelines(f"{website} | {username} | {password}\n")
                entry_web.delete(0, END)
                entry_pass.delete(0, END)
                entry_web.focus()
    else:
        messagebox.showwarning("Oops", "Please dont leave any fields empty!")
    return


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry("720x480")
window.resizable(False, False)
window.title("Password Generator")
window.config(pady=80, padx=80)

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

website_entry = Entry(window, width=30, font=("Courier", 12))
website_entry.grid(column=1, columnspan=2, row=1, pady=5, sticky="w")
website_entry.focus()
username_entry = Entry(window, width=30, font=("Courier", 12))
username_entry.grid(column=1, columnspan=2, row=2, pady=5, sticky="w")
username_entry.insert(0, "maulanafaisal147@gmail.com")

pass_entry = Entry(window, width=20, font=("Courier", 12))
pass_entry.grid(column=1, row=3, pady=5, sticky="w")

generate_button = Button(window, text="Generate", font=("Courier", 12), command=lambda: generate_pass(pass_entry))
generate_button.grid(column=2, row=3, pady=5, sticky="w")

add_button = Button(window, width=30, text="Add", font=("Courier", 12, "bold"), bg="#4D2DB7",
                    command=lambda: save_password(entry_web=website_entry,
                                                  entry_pass=pass_entry,
                                                  entry_username=username_entry))
add_button.grid(column=1, columnspan=2, row=4, pady=5)

window.mainloop()
