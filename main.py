import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

root = tk.Tk()
root.title("Python AI Search")
root.configure(bg='light blue')
root.geometry("400x300")

Label(root, text="Enter your Text", fg="white", bg="black", font=("Helvetica", 18)).pack(pady=30)
entry = Entry(root, width=50, font=("Helvetica", 17))
entry.pack(pady=10)

Button(root, text="Search on YouTube", command=search_youtube, bg="red", fg="white", font=("Helvetica", 12)).pack(pady=10)
Button(root, text="Search on Google", command=search_google, bg="blue", fg="white", font=("Helvetica", 12)).pack(pady=10)

Label(root, text="Made by Dhairya Panchal", fg="black", bg="light blue", font=("Helvetica", 10, "italic")).pack(side="bottom", pady=10)

root.mainloop()


