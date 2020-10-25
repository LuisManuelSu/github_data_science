# Class Creation in Object Oriented Python. This Will create objects of the type "Car" from a list, and
# will ask to the user for adding a new car to the list

#This is the creation of the Class "Car"
class Car:
    def __init__(self, make='Manufacturer', model='Model', color='Color', year='Year', price='Price'):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return '- Brand: {}, Model: {}, Color: {}, Year: {} Price: ${}.'.format(self.make, self.model, self.color, self.year, self.price)

    def make_make(self):
        make = input('Add the brand/manufacturer of the car:\n>>>')
        self.make = make

    def make_model(self):
        model = input('Add the model of the car:\n>>>')
        self.model = model

    def make_color(self):
        color = input('Add the color of the car:\n>>>')
        self.color = color

    def make_year(self):
        while True:
            try:
                year = int(input('Add the year of manufactoring of the car:\n>>>'))
            except Exception:
                print('Invalid Data. Please enter a number')
                continue
            if year < 0:
                print('Invalid Data. Please enter a number over "0"')
                continue
            else:
                self.year = year
                break

    def make_price(self):
        while True:
            try:
                price = int(input('Add the price of the car:\n>>>'))
            except Exception:
                print('Invalid Data. Please enter a number')
                continue
            if price < 0:
                print('Invalid Data. Please enter a number over "0"')
                continue
            else:
                self.price = price
                break

models = []
# Create an intance of the class Car for each car in the cars.cvs file
def list_models():
    print('This are the list of cars included in the store:')
    with open('cars.csv', 'r') as fileref:
        fileref = fileref.readlines()[1:]
        for car in fileref:
            make, model, color, year, price = car.rstrip().split(',')
            new_car = Car(make, model, color, int(year), int(price))
            models.append(new_car)
    sorted_models = sorted(models, key=lambda model: model.year, reverse=True)
    print(*sorted_models, sep='\n')

list_models()
# Ask the user if they want to add a new car to the store and if yes, include it
while True:
    user = input('Do you want to add a new car to the store (y/n):\n>>>')
    if user != 'n' and user != 'y':
        print('Please, type "y" to add a new car or "n" to exit')
        continue
    elif user == 'y':
        new_car = Car()
        new_car.make_make()
        new_car.make_model()
        new_car.make_color()
        new_car.make_year()
        new_car.make_price()
        print(new_car)
        with open('cars.csv', 'a') as fileref:
            fileref.write('{},{},{},{},{}\n'.format(new_car.make, new_car.model, new_car.color, new_car.year, new_car.price))
        models.append(new_car)
        continue
    else:
        break
