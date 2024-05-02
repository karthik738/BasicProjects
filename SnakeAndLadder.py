import tkinter as tk

# main window
root = tk.Tk()
root.geometry("400x400")
root.title("Hello tkinter")
# Create a label widget with "Hello, Tkinter!" text
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20))
label.pack()
w = tk.Button(root, text="Button", activebackground="blue")

# Start the Tkinter event loop
root.mainloop()
