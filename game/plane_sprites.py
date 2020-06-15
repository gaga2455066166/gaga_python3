import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprites(pygame.sprite.Sprite):
    """
    飞机大战的游戏精灵
    """

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprites):
    """
    游戏背景精灵
    """

    def __init__(self, is_alt=False):
        """
        将图片的载入，转移得到类的内部
        """
        super().__init__('../images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprites):
    """
    敌人精灵
    """

    def __init__(self):
        super().__init__('../images/enemy1.png')
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print('飞出屏幕了')
            self.kill()

    def __del__(self):
        # print('敌人被销毁了')
        pass


class Hero(GameSprites):
    """
    英雄精灵类
    """

    def __init__(self):
        super().__init__('../images/hero3.png', 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        """
        英雄在水平方向移动
        :return:
        """
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print('fire')
        # for i in (0, 1, 2):
        #     bullet = Bullet()
        #     bullet.rect.bottom = self.rect.y - i * 40
        #     bullet.rect.centerx = self.rect.centerx
        #     self.bullets.add(bullet)

        bullet = Bullet()
        bullet.rect.bottom = self.rect.y
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)


class Bullet(GameSprites):
    """
    子弹的精灵类
    """

    def __init__(self):
        super().__init__('../images/power1.png', -4)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print('子弹销毁')
        pass
