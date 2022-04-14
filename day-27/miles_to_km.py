from tkinter import *
window = Tk()
window.title("MY PROGRAM")
window.minsize(600, 300)

def mile_converter(miles):
    return miles * 1.609344
def button_clicked():
    result.config(text=mile_converter(int(input.get())))
input = Entry()
input.grid(column=1, row=0)

result = Label()
result.grid(column=1, row=1)

label = Label(text="Miles")
label.grid(column=3, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_result = Label(text="Km")
km_result.grid(column=3, row=1)

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)


window.mainloop()