class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.__steps = 0
        self._calories_burned = 0.0
        pass

    def add_steps(self, steps):
        if steps > 0:
            self.__steps += steps
            print(f'{steps} steps added. Total Steps: {self.__steps}')
        else:
            print('Steps must be positive')
    def get_steps(self):
        return self.__steps
    def add_calories(self, calories):
        if calories > 0:
            self.__calories_burned += calories
            print(f'{calories} calories burned. Total calories bured: {self.__calories_burned}.')
        else:
            print('calories must be postive')
    def get_calories_burned(self):
        return self.__calories_burned
    def reset_tracker(self):
        self.__steps = 0
        self._calories_burned = 0.0
        print('Tracker reset')
              
tracker = FitnessTracker("John")

tracker.add_steps(5000)
tracker.add_steps(1000)
tracker.reset_tracker()
tracker.add_steps(2500)
tracker.get_steps


class Car:
    def __init__(self, color,year, make, model):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        pass
    def drive(self):
        print(f"{self.make} {self.model}is on the road!")
    def wash(self):
        pass
car_1_color = input('car color: ')
car_1_year = int(input('car year: '))
car_1_make = input('car make: ').upper()
car_1_model = input('car model: ').upper()
car_1 = Car(car_1_color, car_1_year, car_1_make, car_1_model)
car_1.drive()