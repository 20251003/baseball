import random
from player import Player
class Game:
    def __init__(self,Pitcher,Hiter):
        self.pitcher = Pitcher
        self.hiter = Hiter
    
    def pitcher_turn(self):

        pitch_straight_speed = self.pitcher.velocity
        pitch_changeup_speed = int(self.pitcher.velocity*0.9)

        #0 : 직구, 1 : 체인지업, 2 : 커브, 3 : 슬라이더
        pitching_data = {
            0 : {
                'type' : 'fastball',
                'ability' : self.pitcher.fastball
            },
            1 : {
                'type' : 'changeup',
                'ability' : self.pitcher.changeup
            },
            2 : {
                'type' : 'curveball',
                'ability' : self.pitcher.curveball
            },
            3 : {
                'type' : 'slider',
                'ability' : self.pitcher.slider
            }
        }
        
        for i in range(6):
            pitch_type = random.randint(0,len(pitching_data))
            if pitch_type == 0:
                numbers = list(range((pitch_straight_speed-9),(pitch_straight_speed+11)))
            else:
                numbers = list(range((pitch_changeup_speed-9),(pitch_changeup_speed+11)))
            weights = [0] * 19
            if self.pitcher.stamina >= 70:
                weights[5:14] = [0.9/10]*10
                weights[15:20] = [0.1/5]*5
            elif self.pitcher.stamina >= 40:
                weights[:4] = [0.2/5]*4
                weights[5:14] = [0.7/10]*10
                weights[15:20] = [0.1/5]*5
            else:
                weights[:4] = [0.4/5]*4
                weights[5:14] = [0.5/10]*10
                weights[15:20] = [0.1/5]*5
            pitch_result = random.choices(numbers,weights=weights,k=1)[0]
            print(f"speed: {pitch_result} km, pitch type: {pitching_data[pitch_type]['type']}, stamina: {self.pitcher.stamina}")
            self.pitcher.stamina = self.pitcher.stamina - 1

