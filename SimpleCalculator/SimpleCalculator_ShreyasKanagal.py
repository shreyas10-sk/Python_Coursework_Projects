import tkinter as tk

def update_display(value):
    # This function updates the display with the new value
    current_text = display_var.get()
    new_text = current_text + str(value)
    display_var.set(new_text)

def clear_display():
    # This function clears the display
    display_var.set("")

def evaluate_expression():
    # This function evaluates the expression in the display
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar to hold the display value
display_var = tk.StringVar()

# Create the display entry widget
display_entry = tk.Entry(
    root,
    textvariable=display_var,
    font = ("Times New Roman", 21),
    bd = 10,
    insertwidth = 2,
    justify = "right",
)
display_entry.grid(row=0, column=0, columnspan=4)

# Define the button labels and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

#Create and place the buttons
for (text, row, col) in buttons:
    if text == '=':
      btn = tk.Button(root, text=text, padx=20, pady=20, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=clear_display)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: update_display(t))

    btn.grid(row=row, column=col, sticky="nsew")

# Start the main loop
root.mainloop()  


