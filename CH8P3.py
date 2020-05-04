from breezypythongui import EasyFrame
class bouncy(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, title = "Tempature Conversion")
    self.addLabel(text = "Fahrenheit", row = 0, column = 0)
    self.fahrenheit = self.addFloatField(value = 32.00, row = 1, column = 0, width = 15, precision = 2)
    self.addLabel(text = "Celsius", row = 0, column = 1)
    self.celsius = self.addFloatField(value = 0.00, row = 1, column = 1, width = 15, precision = 2)
    self.addButton(text = ">>>>", row = 2, column = 0, columnspan = 1, command = self.FtoC)
    self.addButton(text = "<<<<", row = 2, column = 1, columnspan = 2, command = self.CtoF)
  def FtoC(self):
    F = self.fahrenheit.getNumber()
    celsius = (F - 32) * 5/9
    self.celsius.setNumber(celsius)
  def CtoF(self):
    C = self.celsius.getNumber()
    fahrenheit = (C/5) * 9 + 32
    self.fahrenheit.setNumber(fahrenheit)
def main():
  bouncy().mainloop()
if __name__ == "__main__":
  main()
