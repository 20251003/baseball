# main.py
from player import Pitcher  # pitcher 모듈에서 Pitcher 클래스 임포트
from game import Game  # game 모듈에서 Game 클래스 임포트

# Pitcher 인스턴스 생성
pitcher1 = Pitcher()
pitcher1.pitch_speed = 100
pitcher1.stamina = 100

# Game 인스턴스 생성 및 게임 시작
game1 = Game(pitcher1)
game1.pitcher_turn()

# Pitcher 정보 출력
print(pitcher1)
