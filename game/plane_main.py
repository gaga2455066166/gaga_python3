import random
import pygame
from game.plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print('__init__')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        """
        创建精灵组
        :return:
        """
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        """
        事件监听
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print('敌人的机子出现')
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            # print('right')
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            # print('left')
            self.hero.speed = -3
        else:
            # print('0')
            self.hero.speed = 0

    def __check_collide(self):
        """
        碰撞监测
        :return:
        """
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group,
                                   True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        """
        更新并绘制精灵组
        :return:
        """
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        """
        游戏结束
        :return:
        """
        pygame.quit()
        exit()

    def start_game(self):
        """
        游戏循环开始
        :return:
        """
        print('start_game')
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
