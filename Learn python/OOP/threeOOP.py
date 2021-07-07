class Car():

    def __init__(self, speed, power, width, height, trunkSize, heath):
        self.speed = speed
        self.power = power
        self.width = width
        self.height = height
        self.trunkSize = trunkSize
        self.heath =  heath
        print("Car created")

    def move(self):
        print("Moving")

    def loading(self):
        print("Loading")

    def upload(self):
        print("Uploading")

    def broke(self):
        print("Breaking")

    def repair():
        print("Repaired")

class Camaz(Car):

    def __init__(self):
        Car.__init__(self)
        print("Camaz created")

class PassengerCar(Car):

    def __init__(self):
        Car.__init__(self)
        print("Camaz created")



camazOne = Camaz()
print(camazOne.speed)

camazOne.move()
camazOne.loading()
