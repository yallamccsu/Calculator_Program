# Import necessary libraries
import tkinter as tk
from tkinter import StringVar

# Set up the main application window
main_window = tk.Tk()
main_window.geometry('350x400')  # Increased size for better button spacing
main_window.title('My_Calculator')

# Initialize global variables
expression = ''
input_text = StringVar()

# Define button click functions
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ''
    input_text.set('')

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ''
    except:
        input_text.set('Error')
        expression = ''

# Create a frame for the input field
input_frame = tk.Frame(main_window, width=350, height=50, bd=0, highlightbackground='black',
                       highlightcolor='black', highlightthickness=1)
input_frame.pack(side='top')

# Create an entry widget for displaying expressions and results
input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg='#f4f4f4', bd=0, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=15)

# Create a frame for calculator buttons
btns_frame = tk.Frame(main_window, width=350, height=350, bg='#f2f2f2')
btns_frame.pack()

# Define the button layout with improved spacing and color styling
buttons = [
    ('Clear', 0, 0, 4, btn_clear), ('/', 1, 0, 1, lambda: btn_click('/')), ('7', 1, 1, 1, lambda: btn_click(7)), ('8', 1, 2, 1, lambda: btn_click(8)), ('9', 1, 3, 1, lambda: btn_click(9)),
    ('*', 2, 0, 1, lambda: btn_click('*')), ('4', 2, 1, 1, lambda: btn_click(4)), ('5', 2, 2, 1, lambda: btn_click(5)), ('6', 2, 3, 1, lambda: btn_click(6)),
    ('-', 3, 0, 1, lambda: btn_click('-')), ('1', 3, 1, 1, lambda: btn_click(1)), ('2', 3, 2, 1, lambda: btn_click(2)), ('3', 3, 3, 1, lambda: btn_click(3)),
    ('+', 4, 0, 1, lambda: btn_click('+')), ('0', 4, 1, 2, lambda: btn_click(0)), ('.', 4, 3, 1, lambda: btn_click('.')), ('=', 5, 0, 4, btn_equal)
]

# Create buttons dynamically and position them on the grid with added style for better UI
for text, row, col, colspan, command in buttons:
    button_color = '#dcdcdc' if text not in ['/', '*', '-', '+', '=', '.'] else '#ff9f00'  # Color buttons differently based on operator types
    tk.Button(btns_frame, text=text, fg='black', width=10 * colspan, height=3, bd=0, bg=button_color, cursor='hand2', font=('arial', 16, 'bold'), command=command).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# Run the main event loop
main_window.mainloop()
