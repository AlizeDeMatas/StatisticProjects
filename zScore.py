import tkinter as tk

#declare window
window = tk.Tk()
window.title("My Z-Score Calculator")
window.geometry("400x450")
window.configure(background='pink')


#Function

def x_value():
    xVals = int(entry_field1.get())
    meanVals = int(entry_field2.get())
    deviationVals = int (entry_field3.get())
    zScore = float ((xVals - meanVals)/deviationVals)
    return zScore

def zscore_display():
    zScore = x_value()
    calculation_display = tk.Text(master=window, height = 10, width=30)
    calculation_display.grid(column=0,row=13)
    calculation_display.insert(tk.END, zScore)


#LABEL
title = tk.Label(text="Welcome to my Z-Score Calculator App",font=("Comic Sans MS",20),background='pink')
title.grid(row=0, column=0)

#LABEl X Value
label1 = tk.Label(text="Please enter the x value, the score achieved:",font=("Comic Sans", 15, "italic"),background='pink')
label1.grid(row=1, column=0)

#Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(row=2, column=0)

#LABEl mean value
label2 = tk.Label(text="Please enter the mean value of the dataset:",font=("Comic Sans", 15, "italic"),background='pink')
label2.grid(row=3, column=0)

#Entry Field
entry_field2 = tk.Entry()
entry_field2.grid(row=4, column=0)

#LABEl S value
label3 = tk.Label(text="Please enter the s value, the standard deviation:",font=("Comic Sans", 15, "italic"),background='pink')
label3.grid(row=5, column=0)

#Entry Field
entry_field3 = tk.Entry()
entry_field3.grid(row=6, column=0)

#Button
button1 = tk.Button(text="Calculate Z-Score!", command= zscore_display)
button1.grid(row=9, column=0,padx = 10, pady =10 )

#Label
label4 = tk.Label(text="Your Z-Score is...",font=("Comic Sans", 15, "italic"),background='pink')
label4.grid(row=12, column=0)


#run window
window.mainloop()