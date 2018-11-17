class Score:
    def __init(self,name):
        self.team_name = name
        self.try_total = 0
        self.conversion_total = 0
        self.penalty_kick_total = 0
    def try(self):
        self.try_total += 1
    def conversion(self):
        self.conversion_total += 1
    def penalty_kick(self):
        self.penalty_kick_total += 1
    def total_score(self):
        return self.try_total*5+self.conversion_total*2+self.penalty_kick_total*3
    def score_breakdown(self):
        print(self.try_total)
        print(self.conversion_total)
        print(self.penalty_kick_total)

team1 = Score(input("Enter name: "))
team2 = Score(input("Enter name: "))
