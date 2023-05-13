from tkinter import *
py = Tk()
py.title("My First App")
py.geometry("250x170")

def calculator():
    class Cal:
        def __init__(self,a,b):
            self.a=a
            self.b=b
        def add(self):
            sum=self.a+self.b
            return sum

        def sub(self):
            sub=self.a-self.b
            return sub
        def mult(self):
            mul=self.a*self.b
            return mul
        def div(self):
            divi=self.a/self.b
            return divi

    v = input("Enter the operation")
    a = int(input("Enter first no:"))
    b = int(input("Enter second no:"))
    ar = Cal(a,b)
    if v=='+':
        s=ar.add()
        print(s)
    if v=='':
        s=ar.sub()
        print(s)
    if v=='*':
        s=ar.mult()
        print(s)
    if v=='/':
        s=ar.div()
        print(s)

name = Label(py,text="First number",bg="black",fg="white")
name.grid(row=0,column=0)

text= Entry(py,background=
"gray71",foreground="#fff",font= ('Sans Serif', 15, 'italic bold'))
text.grid(row=0,column=2)

name = Label(py,text="Second number",bg="black",fg="white")
name.grid(row=2,column=0)

text= Entry(py, background=
"gray71",foreground="#fff",font= ('Sans Serif', 15, 'italic bold'))
text.grid(row=2,column=2)

name1 = Button(py,text="+",bg="black",fg="white")
name1.grid(row=5,column=0)
name2 = Button(py,text="-",bg="black",fg="white")
name2.grid(row=5,column=1)
name3 = Button(py,text="*",bg="black",fg="white")
name3.grid(row=5,column=2)
name4 = Button(py,text="/",bg="black",fg="white")
name4.grid(row=5,column=3)
name = Button(py,text="Calculate",bg="black",fg="white")
name.grid(row=6,column=3)



py.mainloop()