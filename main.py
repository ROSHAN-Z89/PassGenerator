from random import *
from tkinter import *

num = "0123456789"
alphanum = "qwertyuiopasdfghjklzxcvbnm0123456789AQSWDEFTGYHUJIKOLPMNBVCXZ"
salphanum = "qwertyuiopasdfghjklzxcvbnm0123456789AQSWDEFTGYHUJIKOLPMNBVCXZ!@#$%^&*()_-{=+}[]"



def Create_Pass():
    The_Choice = Tchoise.get()
    if The_Choice == "" :
        Result_box.delete(0.0, END)
        Result_box.insert(END, "\n Select the type of password")

    length = int(pass_length.get())
    randPass = []
    for i in range (length):
        randPass.append(choice(The_Choice))

    result = "". join(randPass)

    TheResult = result +"\n"

    Result_box.delete(0.0, END)
    Result_box.insert(END, TheResult)


window = Tk() 
window.geometry("800x500")
window.title ("Password Generator")

# adds icon to the software
window.iconbitmap = (r"C:\\Users\\Pradyut\\OneDrive\\Desktop\\software\\rand.ico") 

Progname = Label(window, font= ("Comic Sans MS", 18 , "bold") , text= "Password Generator (^_^)", fg = "blue")
Progname.grid(row = 1, column = 3, padx= 200, pady=30)

ChooseType = Label(window, font= ("Comic Sans MS" , 14, "bold"), text = "Choose a type among the 3" )
ChooseType.place(relx = .03, rely= .2 )

Tchoise = StringVar()
Numchoise = Radiobutton(window, font= ('Comic Sans MS', 12, 'bold'), text ="Numeric", variable = Tchoise, value = num)
Numchoise.place(relx = .03 , rely = 0.3)

Alphanumchoise = Radiobutton(window, font= ('Comic Sans MS', 12, 'bold'), text ="Alphanumeric", variable = Tchoise, value = alphanum)
Alphanumchoise.place(relx = .03 , rely = 0.35)

specialchoise = Radiobutton(window, font= ('Comic Sans MS', 12, 'bold'), text ="Special", variable = Tchoise, value = salphanum)
specialchoise.place(relx = .03 , rely = 0.4)


size =  Label(window, text = "Size", font = ("Comic Sans MS" , 14, "bold"))
size.place(relx = .65 , rely = 0.4)


pass_length =  Spinbox(window, from_= 8, to =100)   
pass_length.place(relx = 0.72, rely = 0.42 )
pass_length.config(state = "readonly")

GenButton = Button(window, text = "Generate", command=Create_Pass)
GenButton.place(relx = 0.3 , rely = 0.5)


Result_box = Text(window, height = 10, width =100, wrap = WORD )
Result_box.place(relx = 0.1, rely = 0.7)


window.mainloop()