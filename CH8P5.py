import random
from breezypythongui import EasyFrame
class GuessingGame(EasyFrame):
  def __init__(self):
    low = 0
    high = 100
    EasyFrame.__init__(self, title = "Guessing Game")
    self.count = 0
    greeting = "Press new game to start"
    self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NSEW", columnspan = 2)
    self.addLabel(text = "Your number", row = 1, column = 0)
    self.yourNumber = self.addIntegerField(0, row = 1, column = 1)
    self.addLabel(text = "Computer's guess", row = 2, column = 0)
    self.guessField = self.addIntegerField(0, row = 2, column = 1, state = "readonly")
    self.addLabel(text = "Current Guessing Range", row = 3, column = 1)
    self.addLabel(text = "Low:", row = 4, column = 0)
    self.lowField = self.addIntegerField(low, row = 4, column = 2, state = "readonly")
    self.addLabel(text = "High:", row = 5, column = 0)
    self.highField = self.addIntegerField(high, row = 5, column = 2, state = "readonly")
    self.smallButton = self.addButton(text = "Too small", row = 6, column = 0, command = self.smallGuess)
    self.correctButton = self.addButton(text = "Correct", row = 6, column = 1, command = self.correctGuess)
    self.largeButton = self.addButton(text = "Too large", row = 6, column = 2, command = self.largeGuess)
    self.newButton = self.addButton(text = "New game", row = 7, column = 1, command = self.newGame)
  def smallGuess(self):
    self.count += 1
    self.lowField.setNumber(self.guessField.getNumber())
    comNumber = random.randint(self.lowField.getNumber(), self.highField.getNumber())
    self.guessField.setNumber(comNumber)
  def correctGuess(self):
    self.hintLabel["text"] = "Computer guessed it in " + str(self.count) + " attempts!"
    self.smallButton["state"] = "disabled"
    self.correctButton["state"] = "disabled"
    self.largeButton["state"] = "disabled"
  def largeGuess(self):
    self.count += 1
    self.highField.setNumber(self.guessField.getNumber())
    comNumber = random.randint(self.lowField.getNumber(), self.highField.getNumber())
    self.guessField.setNumber(comNumber)
  def newGame(self):
    high = 100
    low = 0
    comNumber = random.randint(low, high)
    self.count = 0
    greeting = "Computer must guess a number between 1 and 100."
    self.hintLabel["text"] = greeting
    self.guessField.setNumber(comNumber)
    self.smallButton["state"] = "normal"
    self.correctButton["state"] = "normal"
    self.largeButton["state"] = "normal"
def main():
  GuessingGame().mainloop()
if __name__ == "__main__":
  main()
