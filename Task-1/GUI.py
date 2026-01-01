import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked
def greet():
    name = name_entry.get()
    if name.strip():
        messagebox.showinfo("Greeting", f"Hello, {name}! Welcome to Tkinter.")
    else:
        messagebox.showwarning("Warning", "Please enter your name.")

# Create the main window
root = tk.Tk()
root.title("Learn GUI with Tkinter")
root.geometry("400x250")  # Width x Height

# Create a Label
label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
label.pack(pady=20)

# Create an Entry widget
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=10)

# Create a Button
greet_button = tk.Button(root, text="Greet Me", font=("Arial", 14), command=greet)
greet_button.pack(pady=10)

# Create an Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=root.destroy)
exit_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
