import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')  
    label.config(text=current_time)  
    print(current_time)
    label.after(1000, update_time)  



root = tk.Tk()
root.title("Relógio Digital")


label = tk.Label(root, font=('calibri', 40, 'bold'), background='pink', foreground='black')
label.pack(anchor='center')

update_time() 
root.mainloop()  



