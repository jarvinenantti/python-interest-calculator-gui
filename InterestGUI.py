from tkinter import *
from Interest import Interest
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class InterestGUI:
    def __init__(self, master):

        frame = Frame(master)  # main frame
        frame.grid()
        
        self.months = []
        self.money = []

        self.exit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.exit.grid(row=13, column=2)

        self.help = Button(frame, text="HELP", fg="green",
                           command=self.create_help)
        self.help.grid(row=0, column=0)

        self.scLabel = Label(frame, text="Starting capital:")
        self.scLabel.grid(row=1, column=1)
        self.sc = Entry(frame)  # startingCapital
        self.sc.grid(row=2, column=1)
        self.sc.delete(0, END)
        self.sc.insert(0, "1000")

        self.ciLabel = Label(frame, text="Monthly investment:")
        self.ciLabel.grid(row=1, column=2)
        self.ci = Entry(frame)  # capitalIncrease
        self.ci.grid(row=2, column=2)
        self.ci.delete(0, END)
        self.ci.insert(0, "50")
        

        self.tyLabel = Label(frame, text="Total time (years):")
        self.tyLabel.grid(row=3, column=1)
        self.ty = Entry(frame)  # years
        self.ty.grid(row=4, column=1)
        self.ty.delete(0, END)
        self.ty.insert(0, "30")
        
        self.iyLabel = Label(frame, text="Investment time (years):")
        self.iyLabel.grid(row=3, column=2)
        self.iy = Entry(frame)  # years
        self.iy.grid(row=4, column=2)
        self.iy.delete(0, END)
        self.iy.insert(0, "5")

        self.intLabel = Label(frame, fg="green",
                            text="Yearly interest (percent):")
        self.intLabel.grid(row=5, column=1)
        self.int = Entry(frame)  # interest
        self.int.grid(row=6, column=1)
        self.int.delete(0, END)
        self.int.insert(0, "8")

        self.infLabel = Label(frame, fg="red",
                              text="Yearly inflation (percent):")
        self.infLabel.grid(row=5, column=2)
        self.inf = Entry(frame)  # inflation
        self.inf.grid(row=6, column=2)
        self.inf.delete(0, END)
        self.inf.insert(0, "0")

        self.variable = IntVar()  # taxes (yes/no) option
        self.checkButton = Checkbutton(frame, text="Reduce taxes (yes)",
                                       variable=self.variable)
        self.checkButton.grid(row=7, column=1)

        self.calc = Button(frame, text="CALC", fg="green",
                           command=self.calculate)  # call calculate function
        self.calc.grid(row=7, column=2)

        self.rgLabel = Label(frame, text="Gross result:", fg="blue")
        self.rgLabel.grid(row=8, column=1)
        self.resultGross = Message(frame, width=100, text="")  # show gross
        self.resultGross.grid(row=9, column=1)

        self.rrLabel = Label(frame, text="Net, inflation adjusted, result:",
                             fg="blue")
        self.rrLabel.grid(row=8, column=2)
        self.resultNet = Message(frame, width=100, text="")  # show net
        self.resultNet.grid(row=9, column=2)

        self.intTotLabel = Label(frame, text="Total interest factor:",
                                 fg="blue")
        self.intTotLabel.grid(row=10, column=1)
        self.interestTotal = Message(frame, width=100, text="")  # show interest
        self.interestTotal.grid(row=11, column=1)

        self.infTotLabel = Label(frame, text="Total inflation factor:",
                                 fg="blue")
        self.infTotLabel.grid(row=10, column=2)
        self.inflationTotal = Message(frame, width=100, text="")  # show inflation
        self.inflationTotal.grid(row=11, column=2)
        
        self.invSumLabel = Label(frame, text="Total money spent:",
                                 fg="blue")
        self.invSumLabel.grid(row=12, column=1)
        self.investmentSum = Message(frame, width=100, text="")  # show investment sum
        self.investmentSum.grid(row=13, column=1)

    """Creates a message window of Toplevel-type"""

    def create_help(self):
        self.top1 = Toplevel()
        self.top1.title("Help")
        self.top1.grid()

        self.msg = Message(self.top1, text=self.open_file("help.txt"))
        self.msg.grid()

        self.close = Button(self.top1, text="Close", command=self.top1.destroy)
        self.close.grid()

    """Return a String that contains text of 'file_name'"""

    def open_file(self, file_name):
        f = open(file_name, 'r')
        text = f.read()
        return text

    """This method creates an instance of Interest class,
    and sets the values result according to calculations"""

    def calculate(self):
        try:
            self.result = Interest(int(self.sc.get()), int(self.ci.get()),
                                  int(self.int.get()), int(self.inf.get()),
                                  int(self.ty.get()), int(self.iy.get()),
                                  int(self.variable.get()))  # Interest object
            # Months and money could be used to create image (plot)
            self.months = self.result.months
            self.money = self.result.scg
            self.resultNet.config(text=int(self.result.scn),
                                           fg="blue", font=10)  # set net result
            self.resultGross.config(text=int(self.result.scgs),
                                             fg="blue", font=10)  # set gross result
            self.interestTotal.config(
                text=round(float(self.result.intTot), 2),
                fg="blue", font=10)  # set total int           
            self.inflationTotal.config(
                text=round(float(self.result.infTot), 2),
                fg="blue", font=10)  # set total inf
            self.investmentSum.config(
                text=round(float(self.result.scs), 2),
                fg="blue", font=10)  # set total sum
        except ValueError:
            self.resultNet.config(
                text="Please, fill every entry, with numbers only", fg="red")


if __name__ == "__main__":
    root = Tk()  # create instance of Tkinter
    root.title("Investment calculator")
    gui = InterestGUI(root)  # create instance of GUI
    root.mainloop()
    root.destroy()
