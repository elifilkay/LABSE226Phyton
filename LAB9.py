import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='your password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS marvel")
cursorObject.close()

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='your password',
    database='marvel'
)
cursorObject2 = connection.cursor()

cursorObject2.execute('''CREATE TABLE IF NOT EXISTS MarvelInfo(
                            ID int(3) NOT NULL,
                            Movie varchar(80) NOT NULL,
                            DateInfo varchar(50) NOT NULL,
                            Mcu_Phase varchar(50)
                        )''')

id_holder=list()
holder=dict()
with open("Marvel.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            movie_info = line.split()
            movie_id = int(movie_info[0])
            movie_name = movie_info[1]
            date_time = movie_info[2]
            mcu_phase = movie_info[3]
            id_holder.append(movie_id)
            holder[movie_id]=movie_name
            mySql_insert = """INSERT INTO MarvelInfo (ID,Movie,DateInfo,Mcu_Phase)
                                                      VALUES (%s,%s,%s,%s)"""
            values = (movie_id, movie_name, date_time, mcu_phase)

            cursorObject2.execute(mySql_insert, values)

connection.commit()

def updateTextBox(*args):
    selectedItem= dropdown_var.get()
    for key in holder.keys():
        if selectedItem == 'ID':
            text_box.delete(0, tk.END)
            break
        if int(key) == int(selectedItem):
            text_box.delete(0, tk.END)
            text_box.insert(tk.END, holder[key])
            break

def add_to_database(id_entry, movie_entry, date_entry, phase_entry):
    id_value = id_entry.get()
    movie_value = movie_entry.get()
    date_value = date_entry.get()
    phase_value = phase_entry.get()
    with open("Marvel.txt", 'a') as file:
        file.write("\n"+id_value+" "+movie_value+" "+date_value+" "+phase_value)
    mySql_insert = """INSERT INTO MarvelInfo (ID,Movie,DateInfo,Mcu_Phase)
                                                          VALUES (%s,%s,%s,%s)"""
    values = (id_value, movie_value, date_value, phase_value)
    cursorObject2.execute(mySql_insert, values)
    connection.commit()
    if id_value and movie_value and date_value and phase_value:
        messagebox.showinfo("Success", "Data added to the database!")
    else:
        messagebox.showwarning("Error", "Please fill in all fields!")

def open_popup_box():
    popup_box = tk.Toplevel(window)
    popup_box.title("Add Data")
    popup_box.geometry("300x200")

    id_label = tk.Label(popup_box, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(popup_box)
    id_entry.pack()

    movie_label = tk.Label(popup_box, text="Movie:")
    movie_label.pack()

    movie_entry = tk.Entry(popup_box)
    movie_entry.pack()

    date_label = tk.Label(popup_box, text="Date:")
    date_label.pack()

    date_entry = tk.Entry(popup_box)
    date_entry.pack()

    phase_label = tk.Label(popup_box, text="MCU Phase:")
    phase_label.pack()

    phase_entry = tk.Entry(popup_box)
    phase_entry.pack()

    ok_button = tk.Button(popup_box, text="Ok", command=lambda: add_to_database(id_entry, movie_entry, date_entry, phase_entry))
    ok_button.pack(side=tk.LEFT, padx=10)

    cancel_button = tk.Button(popup_box, text="Cancel", command=popup_box.destroy)
    cancel_button.pack(side=tk.RIGHT, padx=10)

def listAllData():
    cursorObject2.execute("SELECT * FROM MarvelInfo")
    result=cursorObject2.fetchall()
    list_window = tk.Toplevel()
    list_window.title("All Data")
    text_box = tk.Text(list_window, width=30, height=30)
    text_box.pack()
    for row in result:
        text_box.insert(tk.END, f"ID: {row[0]}\n")
        text_box.insert(tk.END, f"Movie: {row[1]}\n")
        text_box.insert(tk.END, f"Date: {row[2]}\n")
        text_box.insert(tk.END, f"MCU Phase: {row[3]}\n")
        text_box.insert(tk.END, "\n")

window = tk.Tk()
window.title('Marvel')

box_frame = ttk.Frame(window, padding="20")
box_frame.grid(row=0, column=0)

button1 = ttk.Button(box_frame, text="Add", command=open_popup_box)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = ttk.Button(box_frame, text="List All", command=listAllData)
button2.grid(row=0, column=1, padx=5, pady=5)
text_box = ttk.Entry(box_frame, width=30)
text_box.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

dropdown_var = tk.StringVar()
dropdown_var.trace('w',updateTextBox)
dropdown = ttk.Combobox(box_frame, textvariable=dropdown_var)
dropdown['values'] = ["ID"] + [i for i in range(1,id_holder[-1]+1)]
dropdown.current(0)
dropdown.grid(row=1, column=0, columnspan=3, padx=6, pady=6)


window.mainloop()
connection.close()
cursorObject2.close()