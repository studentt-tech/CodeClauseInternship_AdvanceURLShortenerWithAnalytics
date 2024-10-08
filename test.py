from tkinter import *
import pyshorteners
import requests

root = Tk()
root.title('Url-Shortener')

root.geometry("500x500")

frame=Frame(root,bg="red")
frame.pack(fill=Y)
backgroundimage=PhotoImage(file="im2.png")
Label(frame,image=backgroundimage).pack()
def shorten():
    if shorty.get():
        shorty.delete(0, END)

    if my_entry.get():
        
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        
        shorty.insert(END, url)

def expand():
    short_url = shorty.get()
    if short_url.startswith("http://tinyurl.com/"):
       
        response = requests.head(short_url, allow_redirects=True)
        original_url = response.url
        expanded_url.delete(0, END)
        expanded_url.insert(END, original_url)
    else:
        expanded_url.delete(0, END)
        expanded_url.insert(END, "Not a TinyURL")

my_label = Label(root, text="Enter Link to Shorten", font=("Helvetica", 34))
my_label.pack(pady=20)
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

my_button = Button(root, text="Shorten Link", command=shorten, font=("Helvetica", 24))
my_button.pack(pady=20)

shorty_label = Label(root, text="Shortened Link", font=("Helvetica", 14))
shorty_label.pack(pady=20)

shorty = Entry(root, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=10)

expand_button = Button(root, text="Expand TinyURL", command=expand, font=("Helvetica", 14))
expand_button.pack(pady=10)

expanded_url_label = Label(root, text="Expanded URL", font=("Helvetica", 14))
expanded_url_label.pack(pady=10)

expanded_url = Entry(root, font=("Helvetica", 14), justify=CENTER, width=30, bd=0, bg="systembuttonface")
expanded_url.pack(pady=10)

root.mainloop()
