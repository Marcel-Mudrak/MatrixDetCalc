import numpy as np
from tkinter import ttk
from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl3 = Label(win, text='Result:')
        self.t1 = Entry(bd=3, width=2)
        self.t2 = Entry(bd=3, width=2)
        self.t3 = Entry(bd=3, width=2)
        self.t4 = Entry(bd=3, width=2)
        self.t5 = Entry(bd=3, width=2)
        self.t6 = Entry(bd=3, width=2)
        self.t7 = Entry(bd=3, width=2)
        self.t8 = Entry(bd=3, width=2)
        self.t9 = Entry(bd=3, width=2)
        self.t10 = Entry(bd=3, width=2)
        self.t11 = Entry(bd=3, width=2)
        self.t12 = Entry(bd=3, width=2)
        self.t13 = Entry(bd=3, width=2)
        self.t14 = Entry(bd=3, width=2)
        self.t15 = Entry(bd=3, width=2)
        self.t16 = Entry(bd=3, width=2)

        self.t17 = Entry(bd=3, width=7)

        self.t1.place(x=30, y=10)
        self.t2.place(x=70, y=10)
        self.t3.place(x=110, y=10)
        self.t4.place(x=150, y=10)
        self.t5.place(x=30, y=50)
        self.t6.place(x=70, y=50)
        self.t7.place(x=110, y=50)
        self.t8.place(x=150, y=50)
        self.t9.place(x=30, y=90)
        self.t10.place(x=70, y=90)
        self.t11.place(x=110, y=90)
        self.t12.place(x=150, y=90)
        self.t13.place(x=30, y=130)
        self.t14.place(x=70, y=130)
        self.t15.place(x=110, y=130)
        self.t16.place(x=150, y=130)

        self.btn1 = ttk.Button(win, text='Calculate', command=self.calculate)
        self.btn1.place(x=60, y=180)

        self.lbl3.place(x=30, y=220)
        self.t17.place(x=80, y=217)

    def calculate(self):

        self.t17.delete(0, 'end')
        n1 = int(self.t1.get())
        n2 = int(self.t2.get())
        n3 = int(self.t3.get())
        n4 = int(self.t4.get())
        n5 = int(self.t5.get())
        n6 = int(self.t6.get())
        n7 = int(self.t7.get())
        n8 = int(self.t8.get())
        n9 = int(self.t9.get())
        n10 = int(self.t10.get())
        n11 = int(self.t11.get())
        n12 = int(self.t12.get())
        n13 = int(self.t13.get())
        n14 = int(self.t14.get())
        n15 = int(self.t15.get())
        n16 = int(self.t16.get())

        matrix = np.array([[n1, n2, n3, n4], [n5, n6, n7, n8], [n9, n10, n11, n12], [n13, n14, n15, n16]])

        result = round(np.linalg.det(matrix), 3)

        self.t17.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Matrix Calc')
window.geometry("215x250")
window.mainloop()
