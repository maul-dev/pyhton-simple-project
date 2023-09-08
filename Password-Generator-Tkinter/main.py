from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, randint, shuffle
import pyperclip
import json


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
    website = entry_web.get().lower()
    username = entry_username.get()
    password = entry_pass.get()
    if website and username and password:
        new_data = {
            website: {
                "email": username,
                "password": password,
            }
        }

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are details entered:\n Email/Username: {username}\n "
                                               f"Password: {password}\n its ok to save?")
        if is_ok:
            try:
                with open(file="./data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file="./data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open(file="./data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_web.delete(0, END)
                entry_pass.delete(0, END)
                entry_web.focus()
                messagebox.showinfo(title="Success", message="You password has been save")

    else:
        messagebox.showwarning("Oops", "Please dont leave any fields empty!")
    return


# ---------------------------- SEARCH ------------------------------- #
def search_password(entry_website: Entry):
    website = entry_website.get().lower()
    if len(website) == 0:
        return
    try:
        with open(file="./data.json", mode="r") as data_file:
            data = json.load(data_file)
            password_data = data[website]
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data File Found")
    except KeyError as message:
        messagebox.showwarning(title="Error", message=f"No data File name {message}.")
    else:
        username = password_data["email"]
        password = password_data["password"]
        messagebox.showinfo(title=website, message=f"Username: {username}\n Password: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry("720x480")
window.resizable(False, False)
window.title("Password Generator")
window.config(pady=50, padx=50)

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

website_entry = Entry(window, width=20, font=("Courier", 12))
website_entry.grid(column=1, row=1, pady=5, sticky="w")
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

search_butt = Button(window, text="Search", font=("Courier", 12),
                     command=lambda: search_password(entry_website=website_entry))
search_butt.grid(column=2, row=1, pady=5, padx=8, sticky="w")

window.mainloop()
