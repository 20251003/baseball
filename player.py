class PitchType:
    #직구
    fastball = 0
    fastball_potential = 0
    #체인지업
    changeup = 0
    changeup_potential = 0
    #커브
    curveball = 0
    curveball_potential = 0
    #슬라이더
    slider = 0
    slider_potential = 0

class Pitcher(PitchType):
    # 구속
    velocity = 0
    # 구위
    movement = 0
    # 제구
    control = 0
    # 투구 폼 0 = over-hand, 1 = three-quater, 2 = side-arm, 3 = under-hand
    arm_slot = 0 
    # 투수 잠재력 
    pitcher_potential = 0

class Hiter():
    #컨택
    contact = 0
    #파워
    power = 0
    #선구안
    eye = 0
    #삼진 회피
    avoid_k = 0
    #번트
    bunt = 0
    #도루
    stealing = 0
    #주루
    baserunning = 0

class Player(Pitcher,Hiter):
    #키(정수형)
    height = 0
    #몸무게(실수형)
    weights = 0
    #타격 손
    bats = 'left'
    #투구 손
    throws = 'left'
    #스피드
    speed = 0
    #체력
    stamina = 100
    #정신력(0~100)
    mental = 50
