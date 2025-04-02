import pygame

pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

RECTANGLE_COLOR = (255, 0, 0)

top_left = (0, 0)
size = (0, 0)
dragging = False
filled = False  # Флаг для отслеживания состояния прямоугольника
FPS = 60
clock = pygame.time.Clock()
running = True

while running:
    # Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            top_left = event.pos
            size = 0, 0
            dragging = True
        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0],
                    right_bottom[1] - top_left[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0],
                    right_bottom[1] - top_left[1])
            dragging = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                filled = not filled  # Переключаем состояние при нажатии пробела

    # Основная логика игры
    # Отрисовка объектов
    screen.fill(BACKGROUND)  # очистка экрана

    # Рисуем прямоугольник в зависимости от состояния filled
    if filled:
        pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size))  # Заполненный
    else:
        pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)  # Контурный

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()