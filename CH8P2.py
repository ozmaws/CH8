from breezypythongui import EasyFrame
class bouncy(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, title = "Ball Bounce Distance")
    self.addLabel(text = "Height of drop (in feet)", row = 0, column = 0)
    self.height = self.addFloatField(value = 0.0, row = 0, column = 1, width = 15)
    self.addLabel(text = "Ball bounces", row = 1, column = 0)
    self.bounces = self.addIntegerField(value = 0, row = 1, column = 1, width = 15)
    self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.distance)
    self.addLabel(text = "Total distance (in feet)", row = 3, column = 0)
    self.totalDistance = self.addFloatField(value = 0.0, row = 3, column = 1, width = 15, precision = 2, state = "readonly")
  def distance(self):
    index = 0.6
    height = self.height.getNumber()
    bounces = self.bounces.getNumber()
    bounceHeight = height * index
    totalDistance = height + bounceHeight
    count = 1
    while count < bounces:
      count += 1
      height = bounceHeight
      bounceHeight = height * index
      totalDistance = totalDistance + height + bounceHeight
    self.totalDistance.setNumber(totalDistance)
def main():
  bouncy().mainloop()
if __name__ == "__main__":
  main()
