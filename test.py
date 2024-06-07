import pygame
import sys

# 초기화
pygame.init()

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 화면 크기 설정
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('100x100 Box divided into 100 squares')

# 중앙에 위치한 100x100 박스의 좌표 계산
box_size = 100
box_x = (screen_size[0] - box_size) // 2
box_y = (screen_size[1] - box_size) // 2

# 각 칸의 크기 계산
cell_size = box_size // 10

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 흰색으로 채우기
    screen.fill(WHITE)

    # 중앙에 위치한 100x100 박스 그리기
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_size, box_size))

    # 100x100 박스를 10x10 칸으로 나누어 격자 그리기
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, BLACK, (box_x + i * cell_size, box_y + j * cell_size, cell_size, cell_size), 1)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
