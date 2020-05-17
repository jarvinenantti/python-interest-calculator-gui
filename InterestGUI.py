from tkinter import *
from Interest import Interest

class InterestGUI:
    def __init__(self, master):

        frame=Frame(master) #main frame
        frame.grid()

        self.exit=Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.exit.grid(row=13, column=2)

        self.help=Button(frame, text="HELP", fg="green", command=self.create_help)
        self.help.grid(row=0, column=0)

        self.scLabel=Label(frame, text="Starting capital:")
        self.scLabel.grid(row=1, column=1)
        self.sc=Entry(frame) #startingCapital
        self.sc.grid(row=2, column=1)
        self.sc.delete(0, END)
        self.sc.insert(0, "1000")

        self.ciLabel=Label(frame, text="Capital increase (monthly):")
        self.ciLabel.grid(row=3, column=1)
        self.ci=Entry(frame) #capitalIncrease
        self.ci.grid(row=4, column=1)
        self.ci.delete(0, END)
        self.ci.insert(0, "50")

        self.iLabel=Label(frame, fg="green", text="Interest (percent):")
        self.iLabel.grid(row=5, column=1)
        self.i=Entry(frame) #interest
        self.i.grid(row=6, column=1)
        self.i.delete(0, END)
        self.i.insert(0, "8")

        self.infLabel=Label(frame, fg="red", text="Inflation (percent):")
        self.infLabel.grid(row=5, column=2)
        self.inf=Entry(frame) #inflation
        self.inf.grid(row=6, column=2)
        self.inf.delete(0, END)
        self.inf.insert(0, "0")

        self.yLabel=Label(frame, text="Saving time (years):")
        self.yLabel.grid(row=7, column=1)
        self.y=Entry(frame) #years
        self.y.grid(row=8, column=1)
        self.y.delete(0, END)
        self.y.insert(0, "30")

##        self.infTotLabel=Label(frame, text="Total inflation factor:")
##        self.infTotLabel.grid(row=7, column=2)
##        self.infTot=Entry(frame) #total inflation factor
##        self.infTot.grid(row=8, column=2)
##        self.infTot.delete(0, END)
##        self.infTot.insert(0, "0")

        self.calc=Button(frame, text="CALC", fg="green", command=self.calculate) #call calculate method
        self.calc.grid(row=10, column=1)

        self.rrLabel=Label(frame, text="Net, inflation adjusted, result:", fg="blue")
        self.rrLabel.grid(row=11, column=1)

        self.rgLabel=Label(frame, text="Gross result:", fg="blue")
        self.rgLabel.grid(row=11, column=2)

        self.infTotLabel=Label(frame, text="Total inflation factor:", fg="blue")
        self.infTotLabel.grid(row=8, column=2)

        self.resultReal=Message(frame, width=100, text="") #show real result
        self.resultReal.grid(row=12, column=1)

        self.resultGross=Message(frame, width=100, text="") #show gross result
        self.resultGross.grid(row=12, column=2)

        self.inflationTotal=Message(frame, width=100, text="") #show gross result
        self.inflationTotal.grid(row=9, column=2)
   
        self.variable=IntVar()

        self.checkButton=Checkbutton(frame, text="Reduce taxes", variable=self.variable)
        self.checkButton.grid(row=9, column=1)

    """Creates a message window of Toplevel-type"""
    def create_help(self):
        self.top1=Toplevel()
        self.top1.title("Help")
        self.top1.grid()

        self.msg=Message(self.top1, text=self.open_file("help.txt"))
        self.msg.grid()
        
        self.close=Button(self.top1, text="Close", command=self.top1.destroy)
        self.close.grid()

    """Return a String that contains text of 'file_name'"""
    def open_file(self, file_name):
        f=open(file_name,'r')
        text=f.read()
        return text
        

    """This method creates an instance of Interest class,
    and sets the value of result-message according to final amount of money"""
    def calculate(self):
        try:
            self.money=Interest(int(self.sc.get()), int(self.ci.get()), int(self.i.get()), int(self.inf.get()), int(self.y.get())) #Interest object
            if self.variable.get()==0: #no taxes
                self.resultReal.config(text=int(int(self.money.scr)*float(self.money.inftot)), fg="blue", font=10) #set real result (multiply capital with total inflation factor)
                self.resultGross.config(text=int(self.money.scg), fg="blue", font=10) #set gross result
                self.inflationTotal.config(text=float(self.money.inftot), fg="blue", font=10) #set total inflation
            else: #after taxes
                self.taxedMoney=int((int(self.money.scr)-int(self.money.sca))*0.68) #profit minus 32 % (capital - deposits) * 0,68)
                self.atMoney=int(self.money.sca)+self.taxedMoney #Total capital after taxes
                self.resultReal.config(text=int(int(self.atMoney)*float(self.money.inftot)), fg="blue", font=10)
                self.resultGross.config(text=int(self.money.scg), fg="blue", font=10)
        except ValueError:
            self.resultReal.config(text="Please, fill every entry, numbers only", fg="red")

if __name__=="__main__":
    root=Tk() # instance of Tkinter
    root.title("Capital calculator")
    gui=InterestGUI(root) # gui
    root.mainloop()
    root.destroy()
