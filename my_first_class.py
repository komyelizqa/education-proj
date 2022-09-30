class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Собака создана')

    def sit(self):
        print(self.name.title() + 'Собака села')

    def jump(self):
        print(self.name.title() + 'Собака прыгнула ')

my_dog = Dog('Topic ', 4)
print(my_dog.age)

my_dog.jump()



