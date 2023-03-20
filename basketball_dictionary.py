#Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, input_data):
        self.name = input_data["name"]
        self.age = input_data["age"]
        self.position = input_data["position"]
        self.team = input_data["team"]

    def __repr__(self): 
        return "Player: {}, age: {}, Position:{} , Team: {}".format(self.name, self.age, self.position, self.team)


kevin = {
        "name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"
}

player_kevin = Player(kevin) 
print(player_kevin.name) #prints name of player 
print(player_kevin) 

player_jason = Player(jason)
print(player_jason.name) #prints name of player 
print(player_jason) 

player_kyrie = Player(kyrie)
print(player_kyrie.name) #prints name of player 
print(player_kyrie) 


# need a for loop to call and create new player instance

players = [
    {
        "name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", "age":24,  "position": "small forward", "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", "age":32, "position": "Power Foward",  "team": "Philidelphia 76ers"
    },
    {
        "name": "Duy Lyford",  "age":36,  "position": "Center",  "team": "World"
    }
]

new_team = [] ## this is not working 
for player_list in players:
    player = Player(player_list)
    new_team.append(player) 

print(new_team)

