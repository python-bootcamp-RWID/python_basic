class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def start(self):
        print(self.model, ' is started')

    def stop(self):
        print(self.model, ' is stopped')

    def acceslerate(self):
        print(self.model, ' is acceslerate')


suzuki = Car('Suzuki', 'red', 90)
ferrari = Car('Ferrari', 'black', 120)

suzuki.start()
ferrari.start()
suzuki.stop()
ferrari.acceslerate()
ferrari.stop()