import pygame
import sys

# 초기화
pygame.init()

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

# 각 칸의 크기 계산
cell_size = box_x1 // 10

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 흰색으로 채우기
    screen.fill(WHITE)

    # 중앙에 위치한 100x100 박스 그리기
    pygame.draw.rect(screen, BLACK, (box_x1, box_y1, strike_x, strike_y),1)
    pygame.draw.rect(screen, BLACK, (box_x2, box_y2, ball_x, ball_y),1)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
