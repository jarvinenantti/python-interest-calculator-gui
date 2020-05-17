"""A tool for simple interest calculations.
Uses five attributes to count final amount of money, net and gross."""


class Interest:
    def __init__(self, startingCapital, capitalIncrease, interest, inflation, years):
        try:
            self.scr=startingCapital #real
            self.scg=startingCapital #gross
            self.sca=startingCapital #added
            self.ci=capitalIncrease
            self.i=(interest/100.0)+1 #-> *1.??
            print (repr(self.i)+' interest factor')
            self.intTot=1
            self.inf=1-(inflation/100.0) #-> *0.??
            print (repr(self.inf)+' inflation factor')
            self.inftot=1
            self.real=1+(interest/100.0)-(inflation/100.0)
            print (repr(self.real)+' real interest factor')
            self.times=years*12
            self.month=1
            self.counter=0
            
        except TypeError:
            print("Insert numbers only")

        try:
            for self.counter in range(self.times):
                self.scr=self.scr+self.ci
                self.scg=self.scg+self.ci
                self.sca=self.sca+self.ci
                if self.month==12: #December -> add interest
                    #self.scr=self.scr*self.i
                    #self.scg=self.scg*self.i
                    self.month=1
                    self.intTot=self.intTot*self.i
                    self.inftot=self.inftot*self.inf #PROBLEM: goes too small compared to interest in first method
                else:
                    self.month=self.month+1
            self.scr=self.scr*self.intTot
            self.scg=self.scg*self.intTot
        except Exception:
            print("Calculator failed")
            
            

if __name__ == '__main__':
    print("Interest run by itself")
else:
    print("Interest imported")
