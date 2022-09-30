from car_imp import*
from electrical_car import Electric
a4 = Car('audi', 'a4', 2016)
print(a4.description_name())

tesla = Electric('tesla', 'S', 2017)
tesla.battery.descr_battery()
print(tesla.description_name())