#Daphne Kyprianou
class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Pig(Animal):

    def __init__(self, name, colour, weekly_feed_schedule):
        Animal.__init__(self, name)
        self.colour = colour
        self.weekly_feed_schedule = {}

    def give_food(self, day, food):
        self.weekly_feed_schedule[day] = (food)

    def __str__(self):
        return str(self.name) + ', ' + str(self.colour) + ', '  + str(self.weekly_feed_schedule)


class Cow(Animal):

    def __init__(self, name, colour, weekly_feed_schedule):
        Animal.__init__(self, name)
        self.colour = colour
        self.weekly_feed_schedule = {}

    def give_food(self, day, food):
        self.weekly_feed_schedule[day] = (food)

    def __str__(self):
        return str(self.name) + ', ' + str(self.colour) + ', '  + str(self.weekly_feed_schedule)

def main():
    name = input('How should we call our pig? ')
    colour = input('What colour it is? ')
    p = Pig(name, colour, {})
    for i in range(2):
        day = input('What day it is? ')
        food = input('How much did our pig ate today? ')
        p.give_food(day, food)

    name = input('How should we call our cow? ')
    colour = input('What colour it is? ')
    c = Cow(name, colour, {})
    for i in range(2):
        day = input('What day it is? ')
        food = input('How much did our pig ate today? ')
        c.give_food(day, food)

    farm = open('farm_file.txt', 'w')
    farm.write(str(p) + '\n')
    farm.write(str(c))
    farm.close()

    farm = open('farm_file.txt', 'r')
    f = farm.read()
    print(f)
    farm.close()



main()