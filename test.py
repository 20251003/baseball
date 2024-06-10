import pygame
import sys
import random

# 초기화
pygame.init()

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
YELLOW = (255,255,0)

# 화면 크기 설정
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('100x100 Box divided into 100 squares')

# 중앙에 위치한 100x100 박스의 좌표 계산
strike_x = 99
strike_y = strike_x*5/3
ball_x = strike_x*3
ball_y = strike_x*5

box_x1 = (screen_size[0] - strike_x) // 2
box_y1 = (screen_size[1] - strike_y) // 2
box_x2 = (screen_size[0] - ball_x) // 2
box_y2 = (screen_size[1] - ball_y) // 2

choose_x = list(range(box_x2,box_x2+ball_x))
choose_y = list(range(box_y2,box_y2+ball_y))

class Zone:
    def __init__(self):
        self.pitcher_x = random.choice(choose_x)
        self.pitcher_y = random.choice(choose_y)
        self.pitcher_x2 = list(range(self.pitcher_x - 33, self.pitcher_x + 33))
        self.pitcher_y2 = list(range(self.pitcher_y - 55, self.pitcher_y + 55))
        self.pitcher_random_x = random.choice(self.pitcher_x2)
        self.pitcher_random_y = random.choice(self.pitcher_y2)

# Zone 객체 10개 생성
zones = [Zone() for _ in range(100)]

# 각 Zone 객체의 값을 출력
for i, zone in enumerate(zones):
    print(f"Zone {i+1}: x1={zone.pitcher_x}, y1={zone.pitcher_y} / x2={zone.pitcher_random_x}, y2={zone.pitcher_random_y}")

pygame.font.init()
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 흰색으로 채우기
    screen.fill(WHITE)

    # 스트라이크 볼 박스
    pygame.draw.rect(screen, RED, (box_x1, box_y1, strike_x, strike_y),1)
    pygame.draw.rect(screen, BLACK, (box_x2, box_y2, ball_x, ball_y),1)
    #pygame.draw.rect(screen,BLACK,(box_x1,box_y1,33,55),1)
    
    
    for i,zone in enumerate(zones):
        pygame.draw.circle(screen, BLACK, (zone.pitcher_random_x, zone.pitcher_random_y), 15)
        text_surface = font.render(str(i + 1), True, YELLOW)
        text_rect = text_surface.get_rect(center=(zone.pitcher_random_x, zone.pitcher_random_y))
        screen.blit(text_surface, text_rect)

    #pygame.draw.circle(screen,BLACK,(box_x1,box_x2),2)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
