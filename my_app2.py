class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking...')
    
    def speak(self):
        print('Hello my name is ' + self.name + ' and i am ' + str(self.age) + ' years old')

        

john = Person('John', 22)
john.speak()
john.walk()

print('--------')
mariam = Person('Mariam', 18)
mariam.speak()
mariam.walk()