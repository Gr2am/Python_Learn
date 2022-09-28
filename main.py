##

class Vehical():
    def __init__(self, bodystyle):
      self.bodystyle = bodystyle 

class car(Vehical):
    def __init__(self, engine):
      super().__init__("car")
      self.wheels = 4
      self.doors = 4
      self.engine = engine

car1 = car("gas")
car2 = car("Electr")

print(car1.engine)
print(car2.doors)

## Jest comment for lock how the change done between Replit and github