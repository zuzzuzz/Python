class User: 
    def __init__(self, first_name, last_name, email, age, gender,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.gender = gender
        self.pets = False
        self.is_reward_member = False
        self.gold_card_points = 0


# # this method prints all User details on same line  
# display_info = User("Duy,", "Lyford", "duy.lyford@gmail.com", 36)
# print(vars(display_info)) 

# #this method prints all User details on seperate lines
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Pets: {self.pets}")
        print(f"Member: {self.is_reward_member}")
        print(f"Member Points: {self.gold_card_points}")

# duy = User("Duy", "Lyford", "duy.lyford@gmail.com", 36, "Male")
# print(duy.display_info())

    def enroll(self): 

        if self.is_reward_member:
            print("user already a member")
            return False 

        self.pets = True # can I put this here? Do I need another def? 
        self.is_reward_member = True
        self.gold_card_points = 200


    def spend_points(self, amount): 
        # self.gold_card_points -= amount #shortend alterantive  
        self.gold_card_points = self.gold_card_points - amount  

        if self.gold_card_points < amount: 
            "you don't have enough points"
            return 

duy = User("Duy", "Lyford", "duy.lyford@gmail.com", 36, "Male")
nissa = User("Nissa", "Wisuttismarn", "ndwapt@gmail.com","female", 42)


#test methods 
# duy.display_info()
# duy.enroll()
# duy.spend_points(50) 
# duy.display_info()
# duy.enroll()
# duy.pets() ## why does this not work????? 

# nissa.display_info()
# nissa.enroll()
# nissa.display_info()
# nissa.spend_points(80)
# nissa.display_info()

# duy.display_info()
# nissa.display_info()




