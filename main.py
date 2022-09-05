from tkinter import *
from tkinter import messagebox
from random import randint, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_password():
    search_pass = website_entry.get()

    with open("data.json") as p_file:
        input = json.load(p_file)
    if search_pass in input:
        email_h = input[search_pass]["Email"]
        password_h = input[search_pass]["password"]
        messagebox.showinfo(title="Login Credentials", message=f"Email {email_h}\nPassword: {password_h}")
    else:
        messagebox.showerror(title="Error -201", message=f"You haven't save your Credentials for {search_pass}")


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P',
               'R',
               'S', 'U', 'V']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '@']

    random_letters = [choice(letters) for _ in range(randint(5, 8))]
    random_numbers = [choice(numbers) for _ in range(randint(1, 3))]
    random_symbols = [choice(symbols) for _ in range(randint(1, 2))]
    password_list = random_letters + random_symbols + random_numbers
    final = "".join(password_list)
    password_entry.insert(0, final)
    pyperclip.copy(final)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    jsondata_format = {website: {
        'Email': email,
        'password': password
    }

    }
    if website == "" or password == "" or email == "":
        messagebox.showerror(title="Error 301", message="credentials are empty")
    elif len(password) < 5:
        messagebox.showwarning(title="Warning!", message="Password is too weak")


    else:
        is_ok = messagebox.askyesno(title=f"Login Credentials for {website}",
                                    message=f"Email: {email}\n\nPassword: {password}\n\nDo you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    loaded_data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(jsondata_format, data_file, indent=4)
            else:
                loaded_data.update(jsondata_format)
                with open("data.json", "w") as data_file:
                    json.dump(loaded_data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=200, pady=50)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "vikas@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=10)

generate_button = Button(text="Generate Password", width=14, command=password_generator)
generate_button.grid(row=3, column=2, columnspan=3)
add_button = Button(text="Add", width=25, command=add)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(row=1, column=3, pady=5, padx=5)

window.mainloop()
