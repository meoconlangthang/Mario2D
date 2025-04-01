import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Tạo màn hình game với kích thước 800x600
screen = pygame.display.set_mode((991,620))
pygame.display.set_caption("Thêm Background trong Pygame")

# Tải hình nền
background = pygame.image.load("C:\\Users\\duyth\\Desktop\\Mario2D\\image\\background\\Battleground2.png")

# Vòng lặp chính của game
running = True
while running:
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ background lên màn hình
    screen.blit(background, (0, 0))

    # Cập nhật màn hình
    pygame.display.update()

# Thoát Pygame
pygame.quit()
sys.exit()