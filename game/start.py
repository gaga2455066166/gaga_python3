import pygame
from game.plane_sprites import GameSprites

pygame.init()

game_screen = pygame.display.set_mode((480, 700))  # 绘制窗口

background_png = pygame.image.load('../images/background.png')
game_screen.blit(background_png, (0, 0))  # 绘制背景

hero_png = pygame.image.load('../images/hero3.png')
game_screen.blit(hero_png, (200, 600))

pygame.display.update()  # 初始化刷新
clock = pygame.time.Clock()  # 时钟对象

hero_rect = pygame.Rect(200, 500, 62, 63)

enemy = GameSprites('../images/enemy1.png')
enemy1 = GameSprites('../images/enemy1.png', 2)

enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('游戏退出...')
            pygame.quit()
            exit()
    hero_rect.y -= 4
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    game_screen.blit(background_png, (0, 0))  # 绘制背景
    game_screen.blit(hero_png, hero_rect)  # 绘制飞机
    enemy_group.update()
    enemy_group.draw(game_screen)

    pygame.display.update()
    pass

pygame.quit()
