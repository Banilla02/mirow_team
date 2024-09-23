import pygame
import sys

# 초기 설정
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# 블록 크기
BLOCK_SIZE = 40

# 미로 구조 (1은 벽, 0은 길)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 플레이어 초기 위치
player_x, player_y = 1, 1

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def move_player(dx, dy):
    global player_x, player_y
    new_x = player_x + dx
    new_y = player_y + dy

    # 벽(1)이 아닌 경우에만 이동
    if maze[new_y][new_x] == 0:
        player_x, player_y = new_x, new_y

# 게임 루프
running = True
while running:
    screen.fill(BLACK)

    # 미로 그리기
    draw_maze()

    # 플레이어 그리기
    pygame.draw.rect(screen, BLUE, (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_player(-1, 0)
    if keys[pygame.K_RIGHT]:
        move_player(1, 0)
    if keys[pygame.K_UP]:
        move_player(0, -1)
    if keys[pygame.K_DOWN]:
        move_player(0, 1)

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    clock.tick(30)

# 게임 종료
pygame.quit()
sys.exit()
