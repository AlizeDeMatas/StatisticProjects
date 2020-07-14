
import tkinter as tk

window = tk.Tk()
window.title("Central Tendency Calculator")
window.geometry("600x350")
window.configure(background = '#AED6F1')

#LABEL
title = tk.Label(text="Welcome to the Central Tendency Calculator",font=("Comic Sans MS",20),background='#AED6F1',padx = 70)
title.grid(row=0, column=0)

#LABEl DataSet
label1 = tk.Label(text="Please enter your data set:",font=("Comic Sans", 15, "italic"),background='#AED6F1')
label1.grid(row=1, column=0)

#Button
button1 = tk.Button(text="Calculate Central Tendency!")#, command= zscore_display)
button1.grid(row=3, column=0,padx = 10, pady =20 )

#Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(row=2, column=0)

#LABEl mean value
label2 = tk.Label(text="Your Mean Value is: ",font=("Comic Sans", 15, "italic"),background='#AED6F1')
label2.grid(row=4, column=0)

#Entry Field
entry_field2 = tk.Entry()
entry_field2.grid(row=5, column=0)

#LABEl Mode value
label3 = tk.Label(text="Your Mode Value is: ",font=("Comic Sans", 15, "italic"),background='#AED6F1')
label3.grid(row=6, column=0)

#Entry Field
entry_field3 = tk.Entry()
entry_field3.grid(row=7, column=0)

#LABEl Mode value
label3 = tk.Label(text="Your Median Value is: ",font=("Comic Sans", 15, "italic"),background='#AED6F1')
label3.grid(row=8, column=0)

#Entry Field
entry_field3 = tk.Entry()
entry_field3.grid(row=9, column=0)


window.mainloop()