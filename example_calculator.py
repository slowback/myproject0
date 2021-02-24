import tkinter

root = tkinter.Tk()

root.title('Calculator')
root.geometry('270x270')
root['padx'] = 15

for i in range(8):
    root.columnconfigure(i, weight=2)
    root.rowconfigure(i, weight=2)

# Split frame
# f1 = tkinter.Frame(root, background="bisque")
# f2 = tkinter.Frame(root, background="pink")
# f3 = tkinter.Frame(root, background="red")
# f4 = tkinter.Frame(root, background="green")
# f5 = tkinter.Frame(root, background="blue")
# f6 = tkinter.Frame(root, background="brown")
# f1.grid(row=0, column=0, sticky="nsew")
# f2.grid(row=1, column=1, sticky="nsew")
# f3.grid(row=2, column=2, sticky="nsew")
# f4.grid(row=3, column=3, sticky="nsew")
# f5.grid(row=4, column=4, sticky="nsew")
# f6.grid(row=5, column=5, sticky="nsew")

entry1 = tkinter.Entry(root)
entry1.grid(row=0, column=0, sticky='news', columnspan=5 ,rowspan=1)

label1 = tkinter.Button(root, text='C', border=2)
label2 = tkinter.Button(root, text='CE', border=2)
label1.grid(row=1, column=0, sticky='news')
label2.grid(row=1, column=1, sticky='news')

list_number = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*']
list_name = ['label3', 'label4', 'label5', 'label6', 'label7', 'label8',
             'label9', 'label10', 'label11', 'label2', 'label13', 'label14']
count = 0
for row in range(3):
    for col in range(4):
        list_name[row + col] = tkinter.Button(root, text=list_number[count])
        list_name[row + col].grid(row=row + 2, column=col, sticky='news')
        count += 1


label15 = tkinter.Button(root, text='0')
label16 = tkinter.Button(root, text='=')
label17 = tkinter.Button(root, text='/')
label15.grid(row=5, column=0, sticky='news')
label16.grid(row=5, column=1, sticky='news', columnspan=2)
label17.grid(row=5, column=3, sticky='news')

root.mainloop()