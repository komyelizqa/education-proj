class Battery:
    def __init__(self, battery=100):
        self.battery = battery

    def descr_battery(self):
        print('This auto has battery with ' + str(self.battery) + ' kV of power')

class Electric(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_name(self):
        desc = str(self.year) + ' ' + self.model
        return desc.title()

tesla = Electric('tesla', 'S', 2017)
tesla.battery.descr_battery()

