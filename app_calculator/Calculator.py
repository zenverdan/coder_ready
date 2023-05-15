#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk


# In[11]:


import tkinter as tk

# create a new tkinter window
root = tk.Tk()
root.title("Calculator")

# function to perform calculations
def calculate():
    """Perform the calculation based on the user input."""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# create the user interface
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

button1 = tk.Button(root, text="1", width=5, height=2, command=lambda: entry.insert(tk.END, "1"))
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="2", width=5, height=2, command=lambda: entry.insert(tk.END, "2"))
button2.grid(row=1, column=1)

button3 = tk.Button(root, text="3", width=5, height=2, command=lambda: entry.insert(tk.END, "3"))
button3.grid(row=1, column=2)

button4 = tk.Button(root, text="4", width=5, height=2, command=lambda: entry.insert(tk.END, "4"))
button4.grid(row=2, column=0)

button5 = tk.Button(root, text="5", width=5, height=2, command=lambda: entry.insert(tk.END, "5"))
button5.grid(row=2, column=1)

button6 = tk.Button(root, text="6", width=5, height=2, command=lambda: entry.insert(tk.END, "6"))
button6.grid(row=2, column=2)

button7 = tk.Button(root, text="7", width=5, height=2, command=lambda: entry.insert(tk.END, "7"))
button7.grid(row=3, column=0)

button8 = tk.Button(root, text="8", width=5, height=2, command=lambda: entry.insert(tk.END, "8"))
button8.grid(row=3, column=1)

button9 = tk.Button(root, text="9", width=5, height=2, command=lambda: entry.insert(tk.END, "9"))
button9.grid(row=3, column=2)

button0 = tk.Button(root, text="0", width=5, height=2, command=lambda: entry.insert(tk.END, "0"))
button0.grid(row=4, column=1)

button_plus = tk.Button(root, text="+", width=5, height=2, command=lambda: entry.insert(tk.END, "+"))
button_plus.grid(row=1, column=3)

button_minus = tk.Button(root, text="-", width=5, height=2, command=lambda: entry.insert(tk.END, "-"))
button_minus.grid(row=2, column=3)

button_multiply = tk.Button(root, text="*", width=5, height=2, command=lambda: entry.insert(tk.END, "*"))
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(root, text="/", width=5, height=2, command=lambda: entry.insert(tk.END, "/"))
button_divide.grid(row=4, column=3)

button_clear = tk.Button(root, text="Clear", width=5, height=2, command=lambda: entry.delete(0, tk.END))
button_clear.grid(row=4, column=0)

button_equals = tk.Button(root, text="=", width=5, height=2, command=calculate)
button_equals.grid(row=4, column=2)


# In[12]:


# Start the main loop
root.mainloop()


# In[ ]:




