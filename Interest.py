"""A tool for simple interest calculations.
Uses five attributes to count final amount of money, net and gross."""


class Interest:
    def __init__(self, startingCapital, capitalIncrease, interest, inflation,
                 totalYears, investmentYears, reduceTaxes):
        try:
            self.scg = startingCapital  # gross = only interest
            self.scn = startingCapital  # net = also inflation adjusted
            self.ci = capitalIncrease
            self.i = (interest/100.0)+1
            print(repr(self.i)+' yearly interest factor')
            self.intTot = 1  # total interest factor
            self.inf = 1-(inflation/100.0)
            print(repr(self.inf) + ' inflation factor')
            self.infTot = 1  # total inflation factor
            self.real = 1+(interest/100.0)-(inflation/100.0)
            print(repr(self.real)+' yearly real interest factor')
            self.total = totalYears*12  # month is base 'unit' time period
            self.active = investmentYears*12
            self.month = 1
            self.counter = 0
            self.rd = reduceTaxes

        except TypeError:
            print("Insert numbers only")

        try:
            for self.counter in range(self.total):
                # Accumulate total investment sum every month if active
                if self.counter <= self.active:
                    self.scg = self.scg+self.ci
                # December -> add yearly interest
                if self.month == 12:
                    self.month = 1
                    # Accumulate interest and inflation factors once a year
                    self.intTot = self.intTot*self.i
                    self.infTot = self.infTot*self.inf
                else:  # middle of year
                    self.month = self.month+1

            # Calculate gross and net total(final) investment
            self.scs = self.scg
            self.scg = self.scg*self.intTot
            if self.rd == 1:
                self.scg = self.scs + 0.68 * (self.scg-self.scs)
            self.scn = self.scg*self.infTot
        except Exception as e:
            print("Calculations failed, exception:")
            print(e)


if __name__ == '__main__':
    print("Interest run by itself")
else:
    print("Interest imported")
