import tkinter as tk
from tkinter import *

window=Tk()
window.geometry("400x400")
window.title("karamAlrasam")
window.config(background="#ffcba4")
Label(window, text= "  Binary search\n looking for the item you want", font=("Georgia",16),bg="#ffcba4").pack(pady=20)

n=tk.IntVar()
e=tk.StringVar()

def BinarySearch():
  num=n.get()
  m_list=e.get().split(" ")
  start_p, end_p, res=0,len(m_list),False

  while start_p<end_p and not res:
    mid=(start_p+end_p)//2
    if int(m_list[mid])==num:
      res=True
    elif int(m_list[mid])<num:
      start_p=mid+1
    else:
      end_p=mid
  if res:
    Label(window,width=20,font=("Verdana",10),text="The item is found").pack()
  else:
    Label(window,width=20,font=("Verdana",10),text="The item is not found").pack()

Label(window, text= "Enter the numbers saprated with spaces", font=("Comic Sans MS",13),bg="#ff4500").pack()
Entry(window, width=15,relief="solid", textvariable=e).pack()
Label(window, text= "Enter the number you looking for", font=("Comic Sans MS",13),bg="#ff4500").pack()
Entry(window, width=15,relief="solid", textvariable=n).pack()

Button(window, text="Search", font=("Georgia",7), command=BinarySearch,bg="#008000", fg="white").pack()

window.update()
window.mainloop()