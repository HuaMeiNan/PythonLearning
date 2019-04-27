import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0 ,480, 700)
SHUA_XIN_ZHEN_LV = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE= pygame.USEREVENT +1

class GameSprites(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprites):
    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):

        #调用父类方法实现

        super().update()

        #判断是否移出屏幕

        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprites):

    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时指定图片
        super().__init__('./images/enemy1.png')

        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 4)

        #指定敌机的初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 删除飞机屏幕的飞机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print('敌机被删除{0}'.format(self.rect))

class Hero(GameSprites):

    def __init__(self):
        super().__init__('./images/me1.png')
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        #英雄不能移动出屏幕
        #if self.rect.x <= 0 :
         #   self.rect.x = 0

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in range(0,3):
            print("发射子弹")
            bullets = Bullet()
            bullets.rect.centerx = self.rect.centerx
            bullets.rect.bottom = self.rect.y - i*20
            self.bullets_group.add(bullets)


class Bullet(GameSprites):

    def __init__(self):
        super().__init__("./images/bullet2.png", -3)

    def update(self):

        #调用父类方法，让子弹垂直飞行
        super().update()

        #判断子弹是否飞出屏幕
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        print('子弹被销毁')








