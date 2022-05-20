from tkinter import *

window = Tk()
window.config(width=400, height=200, padx=10, pady=10)
window.title("Miles to Km Converter")

user_input = Entry()
user_input.grid(column=1, row=0)

label1 = Label()
label1.config(text="Miles")
label1.grid(column=2, row=0)

label2 = Label()
label2.config(text="is equal to ")
label2.grid(column=0, row=1)

label3 = Label()
label3.config(text="Km")
label3.grid(column=2, row=1)

label4 = Label()
label4.config(text=str(0))
label4.grid(column=1, row=1)


def mile_km():
    miles = float(user_input.get())
    km = round(1.609344 * miles,2)
    label4.config(text=str(km))


btn = Button()
btn.config(text="Calculate",command=mile_km)
btn.grid(column=1, row=2)






window.mainloop()