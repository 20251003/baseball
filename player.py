class Pitcher:
    # 0 = left, 1 = right
    dominant_hand = 0
    # 90~140
    pitch_speed = 0
    # 0~100
    pitch_quality = 0
    #0~100
    pitch_command = 0
    # 0 = over-hand, 1 = three-quater, 2 = side-arm, 3 = under-hand
    pitching_form = 0 
    # 0~100
    stamina = 0
    # 0~100
    defence = 0
    # 0 = straight, 1 = changeup
    pitch_type = 1

    def __str__(self):
        return (f"dominant_hand: {self.dominant_hand}\n"
                f"pitch_speed: {self.pitch_speed}\n"
                f"pitch_quality: {self.pitch_quality}\n"
                f"pitch_command: {self.pitch_command}\n"
                f"pitching_form: {self.pitching_form}\n"
                f"stamina: {self.stamina}\n"
                f"defence: {self.defence}\n"
                f"pitch_type: {self.pitch_type}")
    
#123123