class Pokemon:
    
    def __init__(self, pkmn_json):
        self.name = pkmn_json['ident'].split(": ")[-1]
        self.ability = pkmn_json['baseAbility']
        self.stats = pkmn_json['stats']
        self.item = pkmn_json['item']
        self.moves = pkmn_json['moves']
        self.condition = pkmn_json['condition']
    
    def pkmn_summary(self):
        print(self.name + "\n",
              self.ability + "\n",
              str(self.stats) + "\n",
              str(self.item) + "\n",
              str(self.moves) + "\n",
              str(self.condition) + "\n",
              "-----------------------------" + "\n")
        
class Team:
    
    def __init__(self, team_info_json):
        
        self.team = []
        
        for pkmn_json in team_info_json:
            p = Pokemon(pkmn_json)
            self.team.append(p)
    
    def team_summary(self):
        for pkmn in self.team:
            pkmn.pkmn_summary()
            