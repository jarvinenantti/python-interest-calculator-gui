"""A tool for simple interest calculations.
Uses five attributes to count final amount of money, net and gross."""


class Interest:
    def __init__(self, startingCapital, capitalIncrease, interest, inflation,
                 totalYears, investmentYears, reduceTaxes):
        try:
            self.scs = startingCapital  # keep track of invested money
            self.scg = []  # gross = only interest
            self.scg.append(startingCapital)
            self.snap = [] # snapshot of total money
            self.months = []
            self.ci = capitalIncrease  # monthly
            self.intr = (interest/100.0)+1
            print(repr(self.intr)+' yearly interest factor')
            self.intTot = 1  # total interest factor
            self.inf = 1-(inflation/100.0)
            print(repr(self.inf) + ' inflation factor')
            self.infTot = 1  # total inflation factor
            self.real = 1+(interest/100.0)-(inflation/100.0)
            print(repr(self.real)+' yearly real interest factor')
            self.total = totalYears*12  # month is base 'unit' time period
            self.active = investmentYears*12
            # self.month = 1
            # self.counter = 0
            self.rd = reduceTaxes

        except TypeError:
            print("Insert numbers only")

        month = 1
        counter = 0
        try:
            for counter in range(self.total):
                self.months.append(counter)
                # Accumulate total investment sum every month if still active
                if counter <= self.active:
                    self.scs = self.scs+self.ci
                    self.scg.append(self.ci)
                # December -> add yearly interest
                if month == 12:
                    month = 1
                    # Accumulate interest and inflation factors once a year
                    self.intTot = self.intTot*self.intr
                    self.infTot = self.infTot*self.inf
                    for i in range(0, len(self.scg), 1):
                        self.scg[i] = self.scg[i]*self.intr
                else:  # middle of year
                    month = month+1
                # Snapshot of current money situtation
                self.snap.append(sum(self.scg))

            # Calculate net total(final) investment
            self.scgs = sum(self.scg)
            if self.rd == 1:  # reduce taxes
                self.scgs = self.scs + 0.68 * (self.scgs-self.scs)
            self.scn = self.scgs*self.infTot  # calculate inflation
        except Exception as e:
            print("Calculations failed, exception:")
            print(e)


if __name__ == '__main__':
    print("Interest run by itself")
else:
    print("Interest imported")
