from breezypythongui import EasyFrame
class taxCalculator(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, title = "Tax Calculator")
    self.addLabel(text = "Gross Income", row = 0, column = 0)
    self.grossIncome = self.addFloatField(value = 0.0, row = 0, column = 1, width = 20)
    self.addLabel(text = "Dependents", row = 1, column = 0)
    self.dependents = self.addIntegerField(value = 0, row = 1, column = 1, width = 10)
    self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.calculation)
    self.addLabel(text = "Total tax", row = 3, column = 0)
    self.totalTax = self.addFloatField(value = 0.0, row = 3, column = 1, width = 20, precision = 2, state = "readonly")
  def calculation(self):
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0
    grossIncome = self.grossIncome.getNumber()
    numDependents = self.dependents.getNumber()
    taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
    incomeTax = taxableIncome * TAX_RATE
    self.totalTax.setNumber(incomeTax)
def main():
  taxCalculator().mainloop()
if __name__ == "__main__":
  main()
