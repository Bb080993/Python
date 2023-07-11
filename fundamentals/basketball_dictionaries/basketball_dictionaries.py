players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, 
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, 
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

class Player:
    team_list=[]
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]
        print(self.name)
        Player.team_list.append(self)
        
    @classmethod
    def get_team(cls,list):
        for player in list:
            cls.team_list.append(Player(player))
        print(cls.team_list)

#Player.get_team(players)   


for player in players:
    Player(player)
print(Player.team_list)


player_Kevin=Player(players[0])
player_Jason=Player(players[1])
player_Kyrie=Player(players[2])

