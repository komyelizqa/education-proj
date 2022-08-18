class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km_reading = 0

    def description_name(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_km(self):
        print('Пробег этого авто ' + str(self.km_reading) + ' km')

    def update_km(self, km):
        if km >=self.km_reading:
            self.km_reading = km
        else:
            print("WTF man?")

    def incr_km(self, km):
        if km>=0:
            self.km_reading+= km
        else:
            print('WTF man?')

# my_car = Car('audi', 'A3', 2017)
#
# my_car.update_km(33)
# my_car.incr_km(100)
# my_car.incr_km(-100)
#
#
# my_car.read_km()
