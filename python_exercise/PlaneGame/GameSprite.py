import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
SHUXINZHENLV = 60
ENEMY_TIME = pygame.USEREVENT
BULLET_TIME = pygame.USEREVENT +1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        # 创建精灵属性
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 定义精灵飞行方式
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height


        
        
class Enemy(GameSprite):
    # 创建敌机
    def __init__(self):
        super(Enemy, self).__init__("./images/enemy1.png")
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0
        self.speed = random.randint(1, 4)

    def update(self):
        super().update()

        if self.rect.y > SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__('./images/me1.png')
        self.rect.bottom = SCREEN_RECT.height - self.rect.height
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullet_group = pygame.sprite.Group()


    def update(self):
        self.rect.x += self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire_bullet(self):
        for i in range(0, 3):
            biu = Bullet()
            biu.rect.bottom = self.rect.y - i*10
            biu.rect.centerx = self.rect.centerx
            self.bullet_group.add(biu)



class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet2.png',-3)

    def update(self):
        super().update()

        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        print("销毁子弹")
