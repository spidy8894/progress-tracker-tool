from Tkinter import *
import tkFileDialog
import ttk
import tkMessageBox



class DeathStalker:
    def __init__(self,root):
       label_0 = Label(root,text="UBS AAF Project Progress",width=20,font=("bold", 20))
       label_0.place(x=150,y=53)

       self.label_1 = Label(root, text="Select your LOB",width=20,font=("bold", 15))
       self.label_1.place(x=150,y=130)

       self.wma_bt = Button(root,text="WMA",width=10,font=("bold",10),bg='brown',fg='white',command = lambda: self.btClick(root,"WMA"))
       self.wma_bt.place(x=100,y=180)

       self.wma_bt = Button(root,text="HRIT",width=10,font=("bold",10),bg='brown',fg='white',command = lambda: self.btClick(root,"HRIT"))
       self.wma_bt.place(x=200,y=180)

       self.wma_bt = Button(root,text="F&R",width=10,font=("bold",10),bg='brown',fg='white',command = lambda: self.btClick(root,"F&R"))
       self.wma_bt.place(x=300,y=180)

       self.wma_bt = Button(root,text="IB",width=10,font=("bold",10),bg='brown',fg='white',command = lambda: self.btClick(root,"IB"))
       self.wma_bt.place(x=400,y=180)

    def btClick(self,root,lname):
        window = Toplevel(root)
        window.geometry('600x450')
        window.title(lname+" Project")
        self.maketabs(window)

    def maketabs(self,window):
        nb = ttk.Notebook(window)
        mygreen = "#d2ffd2"
        myred = "#dd0202"

        style = ttk.Style()

        style.theme_create( "yummy", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
            "TNotebook.Tab": {
            "configure": {"padding": [1, 1], "background": mygreen,"hight":200,"width":20 },
            
            "map":       {"background": [("selected", myred)],
                          
                          "expand": [("selected", [1, 1, 1, 0])] } } } )
        

        style.theme_use("yummy")
        nb.grid(row=1,column = 0,columnspan=50,rowspan=19,sticky='NESW')
        tab1 = ttk.Frame(nb)
        
        nb.add(tab1,text="Common Tasks")
        nb.pack(expand=1, fill='both')
        self.tb1Views(tab1,window)

        tab2 = ttk.Frame(nb)
        nb.add(tab2,text="Developer Enviroment")

        tab3 = ttk.Frame(nb)
        nb.add(tab3,text="QA Enviroment")

        tab4 = ttk.Frame(nb)
        nb.add(tab4,text="Prod Enviroment")

    def tb1Views(self,tab1,window):

        scopeLabel = Label(tab1, text="Got Scope Document?")
        appDocLabel= Label(tab1, text="Got Application Document?")
        appConfigDocLabel = Label(tab1, text="Got Application config Document?")
        
        
       
       


root = Tk()
root.geometry('600x450')
root.title("UBS AAF Project Progess Tool v alpha")
f= DeathStalker(root)
root.mainloop()       
