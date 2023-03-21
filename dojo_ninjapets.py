

# implement __init__( first_name , last_name , treats , pet_food , pet )

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ): 
        self.first_name = first_name 
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self): # walk() - walks the ninja's pet invoking the pet play() method
        self.pet.play()
        print("Your pet got exercised today!") 
    
    def feed(self): # feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self

    def bathe(self): # bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self


class Pet: # implement __init__( name , type , tricks):
    def __init__(self, name, type, tricks, noise ): 
        self.name = name 
        self.type = type
        self.tricks = tricks
        self.noise = noise  #why does the color change? 
        self.health = 100 
        self.energy = 100

    def sleep(self): # sleep() - increases the pets energy by 25
        self.energy += 25
        if self.energy < 50:  
            print("Get More Sleep") 
        return self
    
    def eat(self): # eat() - increases the pet's energy by 5 & health by 10
        self.energy += 10
        self.health += 10
        return self

    def play(self): # play() - increases the pet's health by 5
        self.health += 10
        self.energy -= 25 
        return self

    def tricks(self): 
        if self.type == "dog":
            print("sit, speak")
        elif self.type == " cat": 
            print("I do nothing")
        else:
            print("oh well")
        return self

    def noise(self): # noise() - prints out the pet's sound
        if self.type == "dog":   # trying to create a method that calls different animal types.Each type has a different noise 
            print("woof woof") 
        elif self.type == "cat": 
            print("meow meow")
        else: 
            print("Not your pet")
        return self

dog_treats = ["bones","toy" ]
kavi = Pet("Kavi", "dog", ['sit', 'speak'])
pet_food =["chicken", "beef", "lamb"]

duy = Ninja("duy", "lyford", dog_treats, pet_food, kavi)
