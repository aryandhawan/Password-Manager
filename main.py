from tkinter import *
import json
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_symbol+password_numbers+password_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        "email": email,
        "password": password
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message="Don't leave any of the fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read the old data
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        # update the old data
        data[website] = new_data

        # save the updated data
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP --------------------------------------------------------------------------------------------------------------------
from tkinter import *

window=Tk()
window.title('Password manager')
window.config(padx=20, pady=20)
canvas=Canvas(bg='white',width=200,height=200,)
my_image=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=my_image)
canvas.grid(column=1, row=0)

# labels

website_label=Label(text='Website:')
website_label.grid(column=0,row=3)
Email_label=Label(text='Email/username:')
Email_label.grid(column=0,row=4)
password_label=Label(text='Password:')
password_label.grid(column=0,row=6)

#entries

website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=3,columnspan=1)
email_entry=Entry(width=35)
email_entry.insert(0,'name@gmail.com')
email_entry.grid(column=1,row=4,columnspan=2)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=6,columnspan=1)
#------------------------------------------Search----------------------------------------------------------------------------------------------------------------------
def find_password():
    website=website_entry.get()
    try:
        with open('data.json') as data_file:
            data=json.load(data_file)
            if website in data:
                email=data[website]['email']
                password=data[website]['password']
                messagebox.showinfo(title=website,message=f"Email:{email}\n Password:{password}")
    except FileNotFoundError:
        messagebox.showinfo(title='Oops',message='the Data file doesnt exist!')
    else:
        messagebox.showinfo(title='oops',message='No data found')
#buttons
search_button=Button(text='Search',width=13,command=find_password)
search_button.grid(column=3,row=3,columnspan=2)
generate_button=Button(text='Generate password',command=password_generator)
generate_button.grid(column=2,row=6)
add_button=Button(text='Add',width=40,command=save)
add_button.grid(column=1,row=7,columnspan=3)
window.mainloop()
