from customtkinter import *
from tkinter import messagebox

root = CTk()
root.title("Calculator")
root.geometry("350x530")
root.resizable(False, False)
icon_path = os.path.join(os.path.dirname(__file__), "calc.ico")
root.iconbitmap(icon_path)


def update(value):
    entry1.insert(END, curent_value + value)


def b1():
    update("1")


def b2():
    update("2")


def b3():
    update("3")


def b4():
    update("4")


def b5():
    update("5")


def b6():
    update("6")


def b7():
    update("7")


def b8():
    update("8")


def b9():
    update("9")


def bm():
    update("*")


def bmi():
    update("-")


def bp():
    update("+")


def bd():
    update("/")


def bdot():
    update(".")


def b0():
    update("0")


def _backspace():
    entry_text = entry1.get()
    entry_text = entry_text[:-1]
    entry1.delete(0, END)
    entry1.insert(0, entry_text)


def result():
    try:
        temp = entry1.get()
        temp1 = eval(temp)
        entry1.delete(0, END)
        entry1.insert(0, temp1)
    except Exception as e:
        entry1.delete(0, END)
        messagebox.showerror("Error", "Invalid input")


frame1 = CTkFrame(root,
                  fg_color="azure",
                  height=530,
                  width=350,
                  corner_radius=0)
frame1.place(x=0, y=0)

entry1 = CTkEntry(frame1,
                  height=70,
                  width=330,
                  corner_radius=1,
                  border_width=1,
                  font=("Arial Black", 34, "bold"))
entry1.place(x=10, y=20)
curent_value = entry1.get()

button_7 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="7",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b7)
button_7.place(x=10, y=110)

button_8 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="8",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b8)
button_8.place(x=95, y=110)

button_9 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="9",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b9)
button_9.place(x=95 + 85, y=110)

button_mul = CTkButton(frame1,
                       height=70,
                       width=75,
                       text="X",
                       font=("Arial Black", 28, "bold"),
                       corner_radius=4,
                       fg_color="ivory4",
                       text_color="black",
                       hover_color="ivory3", command=bm)
button_mul.place(x=95 + 85 + 85, y=110)

# row 2

button_4 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="4",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b4)
button_4.place(x=10, y=110 + 85)

button_5 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="5",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b5)
button_5.place(x=95, y=110 + 85)

button_6 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="6",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b6)
button_6.place(x=95 + 85, y=110 + 85)

button_div = CTkButton(frame1,
                       height=70,
                       width=75,
                       text="÷",
                       font=("Arial Black", 28, "bold"),
                       corner_radius=4,
                       fg_color="ivory4",
                       text_color="black",
                       hover_color="ivory3",
                       command=bd)
button_div.place(x=95 + 85 + 85, y=110 + 85)

# row 3

button_1 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="1",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b1)
button_1.place(x=10, y=110 + 85 + 85)

button_2 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="2",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b2)
button_2.place(x=95, y=110 + 85 + 85)

button_3 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="3",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b3)
button_3.place(x=95 + 85, y=110 + 85 + 85)

button_sub = CTkButton(frame1,
                       height=70,
                       width=75,
                       text="-",
                       font=("Arial Black", 30, "bold"),
                       corner_radius=4,
                       fg_color="ivory4",
                       text_color="black",
                       hover_color="ivory3",
                       command=bmi)
button_sub.place(x=95 + 85 + 85, y=110 + 85 + 85)

# row 4

button_0 = CTkButton(frame1,
                     height=70,
                     width=75,
                     text="0",
                     font=("Arial Black", 28, "bold"),
                     corner_radius=4,
                     fg_color="ivory4",
                     text_color="black",
                     hover_color="ivory3",
                     command=b0)
button_0.place(x=10, y=110 + 85 + 85 + 85)

button_dot = CTkButton(frame1,
                       height=70,
                       width=75,
                       text=".",
                       font=("Arial Black", 28, "bold"),
                       corner_radius=4,
                       fg_color="ivory4",
                       text_color="black",
                       hover_color="ivory3",
                       command=bdot)
button_dot.place(x=95, y=110 + 85 + 85 + 85)

button_plus = CTkButton(frame1,
                        height=70,
                        width=75,
                        text="+",
                        font=("Arial Black", 30, "bold"),
                        corner_radius=4,
                        fg_color="ivory4",
                        text_color="black",
                        hover_color="ivory3",
                        command=bp)
button_plus.place(x=95 + 85, y=110 + 85 + 85 + 85)

button_back = CTkButton(frame1,
                        height=70,
                        width=75,
                        text="\u232B",
                        font=("Arial Black", 30, "bold"),
                        corner_radius=4,
                        fg_color="ivory4",
                        text_color="black",
                        hover_color="ivory3",
                        command=_backspace)
button_back.place(x=95 + 85 + 85, y=110 + 85 + 85 + 85)

button_equal = CTkButton(frame1,
                         height=70,
                         width=330,
                         text="=",
                         font=("Arial Black", 30, "bold"),
                         corner_radius=4,
                         fg_color="ivory4",
                         text_color="black",
                         hover_color="ivory3",
                         command=result)
button_equal.place(x=10, y=110 + 85 + 85 + 85 + 85)

root.mainloop()
