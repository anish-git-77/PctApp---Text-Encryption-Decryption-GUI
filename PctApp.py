from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()
    
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")

        try:
            base64_bytes = base64.b64decode(encode_message)
            decrypted = base64_bytes.decode("ascii")
        except Exception as e:
            messagebox.showerror("Decryption", "Invalid encoded text")
            return

        Label(screen2, text="DECRYPT", font="Arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypted)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    else:
        messagebox.showerror("Decryption", "Wrong Password")

def encrypt():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypted)
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Wrong Password")

def main_screen():
    global screen
    global code
    global text1
    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    try:
        image_icon = PhotoImage(file="keys.png")
        screen.iconphoto(False, image_icon)
    except Exception as e:
        print("Icon not found. Skipping...")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter the text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Arial 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#00BD56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
